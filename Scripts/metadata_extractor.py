import json
import os
import re
import shutil

import click
import pandas as pd
import pyodbc
import xmltodict


DREMIO_DRIVER = "Dremio ODBC Driver 64-bit"


#
# Extraction functions
#
def parse_dss_xml(path: str,
                  prefix: str) -> pd.DataFrame:
    """
    Parse the DSS configuration file
    """

    pattern = prefix + r"[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+"

    with open(path, 'r') as myfile:
        obj = xmltodict.parse(myfile.read(), encoding="utf-8")

    dictionary = json.loads(json.dumps(obj, ensure_ascii=False), encoding="utf-8")
    resources = dictionary["data"]["resource"]
    queries = dictionary["data"]["query"]

    l = []
    for i in queries:
        idx = i.get("@id")
        for j in resources:
            if j.get("call-query", {}).get("@href") == idx:
                endpoint = j.get("@path")
        sql = i.get("sql")
        table = re.findall(pattern, sql)[0]

        d = {
        "table_full_name": table,
        "dss_query_name": idx,
        "dss_endpoint": endpoint
        }

        if all(d.values()):
            if re.match("^fbk_test1__VISUALIZATION_TABLES.*", table):
                l.append(d)

    return pd.DataFrame(l)


def extract_metadata(cnxn: pyodbc.Connection,
                     filter_spaces: tuple
                     ) -> pd.DataFrame:
    """
    Extract tabels with its definition.
    """
    sql_df = """
             SELECT  TABLE_SCHEMA as table_space,
                     TABLE_NAME as table_name,
                     CONCAT(TABLE_SCHEMA, '.', TABLE_NAME) as table_full_name,
                     VIEW_DEFINITION as table_definition
             FROM    INFORMATION_SCHEMA.VIEWS
             """
    df = pd.read_sql(sql_df, cnxn)
    df = df[df["table_space"].isin(filter_spaces)]
    return df


def extract_raw_schema(cnxn: pyodbc.Connection,
                       filter_spaces: tuple
                       ) -> pd.DataFrame:
    """
    Extract a raw table schema
    """
    sql = """
    SELECT  TABLE_SCHEMA as table_space,
            TABLE_NAME as table_name,
            CONCAT(TABLE_SCHEMA, '.', TABLE_NAME) as table_full_name,
            COLUMN_NAME,
            CASE DATA_TYPE
                WHEN 'CHARACTER VARYING' THEN 'string'
                WHEN 'BIGINT' THEN 'integer'
                WHEN 'DATE' THEN 'date'
                WHEN 'DOUBLE' THEN 'number'
                WHEN 'INTEGER' THEN 'integer'
                WHEN 'TIME' THEN 'time'
                WHEN 'TIMESTAMP' THEN 'datetime'
            END AS DATA_TYPE
    FROM    INFORMATION_SCHEMA.COLUMNS
    """
    df = pd.read_sql(sql,cnxn)
    df = df[df["table_space"].isin(filter_spaces)]
    df["table_schema"] = df.apply(lambda x: {"name": x["COLUMN_NAME"],
                                             "description": cap(x["COLUMN_NAME"]),
                                             "type": x["DATA_TYPE"],
                                             "constraints":{},
                                             "rdfType": "",
                                             "errors": {} }, axis=1)
    df = df.groupby(["table_space",
                     "table_name",
                     "table_full_name"])["table_schema"].apply(list).reset_index()
    return df


def enrich_df(df, prefix):
    """
    Enrich the dataframe with information.
    """

    # Data version
    df["table_version"] = "1.0"

    # Validation section
    df["core_dataset"] = df["table_space"].apply(lambda x: x == "fbk_test1__CORE_DATASET")
    df["require_validation"] = df["table_space"].apply(lambda x: x == "fbk_test1__CORE_DATASET")
    df["origin_dataset"] = df.apply(lambda x: x["table_name"].split("_")[0] if x["table_space"] == "fbk_test1__CORE_DATASET" else "", axis=1)

    # Data exposition section
    df["dss_exposed"] = df["table_space"].apply(lambda x: x == "fbk_test1__VISUALIZATION_TABLES")
    df["format_exposed"] = df["table_space"].apply(lambda x: "JSON" if x == "fbk_test1__VISUALIZATION_TABLES" else "")
    df["format_authentication"] = df["table_space"].apply(lambda x: "Bearer token" if x == "fbk_test1__VISUALIZATION_TABLES" else "")

    # Data genealogy
    df["table_parents"] = df["table_definition"].apply(return_parents, prefix=prefix)
    df["table_children"] = df["table_full_name"].apply(lambda x: return_child(x, df))

    return df


#
# Utils
#
def create_path(path: str) -> None:
    """
    Create folder if not existing.
    """
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except Exception:
            raise


def write_file(text: str, filename: str) -> None:
    """
    Write a file.
    """
    create_path(os.path.dirname(filename))
    with open(filename, "w") as f:
        f.write(text)


def cap(string):
    string = string.split("_")
    string[0] = string[0].capitalize()
    return " ".join(string)


def return_parents(s, prefix: str):
    p = prefix + r"[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+"
    l = sorted(list(set(re.findall(p, s))))
    l = l if l != [] else [""]
    return l


def return_child(s, df):
    l = []
    for i in df.iterrows():
        if s in i[1]["table_parents"]:
            l.append(i[1]["table_full_name"])
    l = sorted(l)
    l = l if l != [] else [""]
    return l


def io_description(path, dic, read_key, new_key, placeholder):
    if os.path.exists(path):
        with open(path, "r") as f:
            dic[new_key] = json.loads(f.read()).get(read_key, placeholder)
    else:
        write_file(json.dumps({new_key: placeholder}, indent=2), path)
        dic[new_key] = placeholder
    return dic


def check_table_schema(path_schema, path_raw):
    if not os.path.exists(path_schema):
        try:
            os.makedirs(os.path.dirname(path_schema))
        except:
            pass
        shutil.copy(path_raw, path_schema)


def read_table_schema(path):
    
    with open(path, "r") as f:
        return json.loads(f.read())


def build_path(*args) -> str:
    return os.path.join(*args)


#
# Main
#
@click.command()
@click.option("--data-path")
@click.option("--xml-path")
@click.option("--dremio-host")
@click.option("--dremio-port")
@click.option("--dremio-user")
@click.option("--dremio-pass")
@click.option("--space-core")
@click.option("--space-master")
@click.option("--space-visual")
@click.option("--prefix")
def main(**kwargs):

    path = kwargs["data_path"]
    xml_path = kwargs["xml_path"]

    cnxn = pyodbc.connect(driver=DREMIO_DRIVER,
                          host=kwargs["dremio_host"],
                          port=kwargs["dremio_port"],
                          user=kwargs["dremio_user"],
                          password=kwargs["dremio_pass"],
                          autocommit=True)

    core = kwargs["space_core"]
    master = kwargs["space_master"]
    visual = kwargs["space_visual"]
    prefix = kwargs["prefix"]

    # Parse the xml dss configuration
    dss = parse_dss_xml(xml_path, prefix)

    # Extract table metadata
    viw = extract_metadata(cnxn, (core, master, visual))
    
    # Extract raw table schema
    sch = extract_raw_schema(cnxn, (core, master, visual))

    # Merge dataframes
    df = viw.merge(sch).merge(dss, how="left")
    df.fillna("", inplace=True)

    # Enrich tables metadata
    df = enrich_df(df, prefix)

    # Reordering columns
    df = df[["table_space",
             "table_name",
             "table_full_name",
             "table_version",
             "table_definition",
             "table_schema",
             "table_parents",
             "table_children",
             "core_dataset",
             "origin_dataset",
             "require_validation",
             "dss_exposed",
             "dss_query_name",
             "dss_endpoint",
             "format_exposed",
             "format_authentication"]]

    # Store metadata (tables structures and tables info)
    for i in df.iterrows():

        name = i[1].table_name
        space = i[1].table_space
        full_name = f"{space}.{name}"
        full_path = build_path(path, space, name)

        # Paths
        path_rscm = build_path(full_path, "raw_schema.json")
        path_tscm = build_path(full_path, "table_schema.json")
        path_info = build_path(full_path, "table_info.json")
        path_desc = build_path(full_path, "table_description.json")
        path_meta = build_path(full_path, "table_metadata.json")

        # Store raw table schema 
        schema = df[df["table_full_name"] == full_name][["table_schema"]].rename(columns = {"table_schema": "fields"})
        schema = schema.to_dict(orient='records')[0]
        write_file(json.dumps(schema, indent=2), path_rscm)
        
        # Check if a refined table schema exists, otherwise copy raw schema
        check_table_schema(path_tscm, path_rscm)

        # Store table info and read table description
        info = df[df["table_full_name"] == full_name].loc[:, df.columns != 'table_schema'].to_dict(orient='records')[0]
        info = io_description(path_desc, info, "table_description", "table_description", "")
        write_file(json.dumps(info, indent=2), path_info)

        # Store full metadata and read table schema
        info["table_schema"] = read_table_schema(path_tscm)
        write_file(json.dumps(info, indent=2), path_meta)

if __name__=="__main__":
    main()

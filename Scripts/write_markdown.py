import glob
import json
import os
import re

import click
import pandas as pd


METADATA_PATH = "*/*/table_metadata.json"
MARKDOWN_PATH = "{}/{}/markdown.md"
PNG_PATH = "./graph_png.png"
README_PATH = "README.md"

TEMPLATE_README = """# SOMMARIO

{}
"""

TEMPLATE_TABLE = """# {}

## Info tabella

{}

## Struttura relazionale

{}

## Descrizione struttura tabella

{}
"""


def format_md_table_link(string: str) -> str:
    """
    Return a markdown formatted link string to a table.
    Example: [SPACE.TAB](/SPACE/markdown/TAB.md)
    """
    capture_group = r"(.+)\.(.+)"
    match = re.match(capture_group, string)
    if match:
        space = match.group(1)
        table = match.group(2)
        return f"[{space}.{table}](/Documentation/{space}/{table}/markdown.md)"
    return string


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
    with open(filename, "w") as file:
        file.write(text)


def read_json(filename: str) -> dict:
    """
    Load json file.
    """
    with open(filename, "r") as file:
        return json.loads(file.read())


def table_to_markdown(table_name: str,
                      table_info: pd.DataFrame,
                      table_img_link: str,
                      table_schema: pd.DataFrame) -> str:
    """
    Wrap table info and table schema into a markdown sheet.
    """
    return TEMPLATE_TABLE.format(table_name,
                                 table_info.to_markdown(index=False),
                                 table_img_link,
                                 table_schema.to_markdown(index=False))

def readme_to_markdown(tables: pd.DataFrame) -> str:
    """
    Wrap table list into a markdown sheet.
    """
    return TEMPLATE_README.format(tables.to_markdown(index=False))


def parse_info(d: dict) -> dict:
    """
    Parse metadata JSON file.
    """
    return {
        "Nome tabella Dremio": [d.get("table_name")],
        "Space Dremio": [d.get("table_space")],
        "Nome completo": [d.get("table_full_name")],
        "Descrizione tabella": [d.get("table_description")],
        "Versione": [d.get("table_version")],
        "Core dataset": [d.get("core_dataset")],
        "Dataset di origine": [d.get("origin_dataset")],
        "Richiede validazione": [d.get("require_validation")],
        "Esposta in DSS": [d.get("dss_exposed")],
        "Endpoint DSS": [d.get("dss_endpoint")],
        "Query name DSS": [d.get("dss_query_name")],
        "Formato esposizione": [d.get("format_exposed")],
        "Tipologia autenticazione": [d.get("format_authentication")],
        "Tabelle genitrici": ["\n".join(map(format_md_table_link,
                                        d.get("table_parents", [""])))],
        "Tabelle figlie": ["\n".join(map(format_md_table_link,
                                         d.get("table_children", [""])))]
    }


@click.command()
@click.option("--data-path")
def main(**kwargs):

    base_path = kwargs["data_path"]
    glob_path = os.path.join(base_path, METADATA_PATH)

    tables_list = []

    for path in glob.glob(glob_path):

        metadata = read_json(path)
        space = metadata.get("table_space")
        name = metadata.get("table_name")
        schema = metadata.pop("table_schema")["fields"]

        # Table info
        info = parse_info(metadata)
        info = pd.DataFrame(info).melt(var_name="Info", value_name="Descrizione")

        # Table schema
        schema = pd.DataFrame(schema).rename(columns={
            "name": "Campo",
            "description": "Descrizione",
            "type": "Tipo",
            "constraints": "Constraints",
            "rdfType": "Linked data",
        })

        # Link to relationship image
        img_link = f"![{name}]({PNG_PATH})"

        # Save markdown file
        out_path_md = os.path.join(base_path, MARKDOWN_PATH.format(space, name))
        string_md = table_to_markdown(name, info, img_link, schema)
        write_file(string_md, out_path_md)

        tables_list.append(f"{space}.{name}")

    # Update README summary
    tables_list = sorted(tables_list)
    out_path_readme = os.path.join(base_path, README_PATH)
    summary = pd.DataFrame({"Tabelle": ["\n".join(map(format_md_table_link, tables_list))]})
    string_readme = readme_to_markdown(summary)
    write_file(string_readme, out_path_readme)


if __name__=="__main__":
    main()

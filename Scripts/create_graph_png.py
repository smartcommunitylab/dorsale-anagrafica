import glob
import json
import os

import click
import pydot


METADATA_PATH = "*/*/table_metadata.json"
PNG_PATH = "{}/{}/graph_png.png"


class GraphNode:

    def __init__(self, id, kind, label, space):
        self.id = id
        self.kind = kind
        self.label = label
        self.space = space


def create_path(path: str) -> None:
    """
    Create folder if not existing.
    """
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except Exception:
            raise


def read_json(filename: str) -> dict:
    """
    Load json file.
    """
    with open(filename, "r") as file:
        return json.loads(file.read())


def parse_entities(metadata: dict) -> dict:
    """
    Parse table metadata.
    """
    return {
        "table_space": metadata.get("table_space"),
        "table_name": metadata.get("table_name"),
        "base_table": [metadata.get("table_full_name")],
        "parents": metadata.get("table_parents", [""]),
        "children": metadata.get("table_children", [""])
    }


def create_graph(entities: dict,
                 core: str,
                 master: str,
                 visual: str) -> pydot.Dot:

    idx = 0
    base_tab_id = None
    nodes = []
    for i in entities:
        for j in entities[i]:
            if j != '':
                tag = j.split(".")
                nodes.append(GraphNode(idx, i, tag[1], tag[0]))

                if i == "base_table":
                    base_tab_id = idx

                idx += 1

    edges = []
    for i in nodes:

        if i.kind == "parents" and i.id != base_tab_id:
            edges.append((i.id, base_tab_id))

        elif i.kind == "children" and i.id != base_tab_id:
            edges.append((base_tab_id, i.id))

    graph = pydot.Dot("my_graph", graph_type="digraph")

    for i in nodes:
        style = {}
        style["label"] = i.label
        style["shape"] = "rect"
        style["style"] = "filled"
        style["colorscheme"] = "pastel13"

        if i.space == core:
            style["fillcolor"] = "1"
        if i.space == master:
            style["fillcolor"] = "2"
        if i.space == visual:
            style["fillcolor"] = "3"

        graph.add_node(pydot.Node(i.id, **style))

    for i in edges:
        graph.add_edge(pydot.Edge(*i))

    return graph


@click.command()
@click.option("--data-path")
@click.option("--space-core")
@click.option("--space-master")
@click.option("--space-visual")
def main(**kwargs):

    base_path = kwargs["data_path"]
    core = kwargs["space_core"]
    master = kwargs["space_master"]
    visual = kwargs["space_visual"]
    
    glob_path = os.path.join(base_path, METADATA_PATH)

    for path in glob.glob(glob_path):

        metadata = read_json(path)

        entities = parse_entities(metadata)

        output_path = os.path.join(base_path, PNG_PATH.format(entities.pop("table_space"),
                                                              entities.pop("table_name")))

        graph = create_graph(entities, core, master, visual)
        create_path(os.path.dirname(output_path))
        graph.write_png(output_path)


if __name__=="__main__":
    main()

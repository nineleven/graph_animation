import pytest

import networkx as nx

from src.render_graph import build_colors_list
from src.constants import Color, GraphElementAttr

from typing import List, DefaultDict, Any, Dict

from collections import defaultdict


class CaseBuildColorList:
    
    def __init__(self, name: str, graph: nx.DiGraph,
                 nodes_attr_dict: Dict[Any, GraphElementAttr],
                 edges_attr_dict: Dict[Any, GraphElementAttr],
                 node_color: List[str], edge_color: List[str]):
        self.name = name
        self.graph = graph
        self.nodes_attr_dict = nodes_attr_dict
        self.edges_attr_dict = edges_attr_dict
        self.node_color = node_color
        self.edge_color = edge_color

    def __str__(self) -> str:
        return 'test_{}'.format(self.name)


TEST_CASES_BUILD_COLOR_LIST = list()

TEST_CASES_BUILD_COLOR_LIST.append(
    CaseBuildColorList(
        'empty_graph',
        nx.DiGraph(),
        dict(),
        dict(),
        [],
        []
    )
)


def default_func() -> GraphElementAttr:
    return GraphElementAttr(Color.COLOR_REST, False)


nodes_attr_dict: DefaultDict[Any, GraphElementAttr] = defaultdict(default_func)
edges_attr_dict: DefaultDict[Any, GraphElementAttr] = defaultdict(default_func)

graph = nx.DiGraph()
graph.add_node('A')
nodes_attr_dict['A'].color = Color.COLOR_PROGRESS
graph.add_node('B')
nodes_attr_dict['B'].color = Color.COLOR_REST
graph.add_edge('A', 'B')
edges_attr_dict[('A', 'B')].color = Color.COLOR_PROGRESS
graph.add_edge('A', 'C')
edges_attr_dict[('A', 'C')].color = Color.COLOR_REST
node_color = [Color.COLOR_PROGRESS.value, Color.COLOR_REST.value, Color.COLOR_REST.value]
edge_color = [Color.COLOR_PROGRESS.value, Color.COLOR_REST.value]

TEST_CASES_BUILD_COLOR_LIST.append(
    CaseBuildColorList(
        'random_graph',
        graph,
        nodes_attr_dict,
        edges_attr_dict,
        node_color,
        edge_color
    )
)


@pytest.mark.parametrize(
    'case',
    TEST_CASES_BUILD_COLOR_LIST,
    ids=str
)
def test_build_color_list(case: CaseBuildColorList) -> None:
    node_color, edge_color = build_colors_list(case.graph, nodes_attr_dict, edges_attr_dict)
    assert node_color == case.node_color and\
           edge_color == case.edge_color

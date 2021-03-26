import pytest

import networkx as nx

from src.draw_graph import build_colors_list
from src.constants import Color, Attr

from typing import List


class CaseBuildColorList:
    
    def __init__(self, name: str, graph: nx.DiGraph,
                 node_color: List[str], edge_color: List[str]):
        self.name = name
        self.graph = graph
        self.node_color = node_color
        self.edge_color = edge_color

    def __str__(self) -> str:
        return 'test_{}'.format(self.name)


TEST_CASES_BUILD_COLOR_LIST = list()

TEST_CASES_BUILD_COLOR_LIST.append(
    CaseBuildColorList(
        'empty_graph',
        nx.DiGraph(),
        [],
        []
    )
)

graph = nx.DiGraph()
graph.add_node('A')
graph.nodes['A'][Attr.ATTR_COLOR] = Color.COLOR_PROGRESS
graph.add_node('B')
graph.nodes['B'][Attr.ATTR_COLOR] = Color.COLOR_REST
graph.add_edge('A', 'B')
graph.edges[('A', 'B')][Attr.ATTR_COLOR] = Color.COLOR_PROGRESS
graph.add_edge('A', 'C')
graph.edges[('A', 'C')][Attr.ATTR_COLOR] = Color.COLOR_REST
node_color = [Color.COLOR_PROGRESS.value, Color.COLOR_REST.value, Color.COLOR_REST.value]
edge_color = [Color.COLOR_PROGRESS.value, Color.COLOR_REST.value]

TEST_CASES_BUILD_COLOR_LIST.append(
    CaseBuildColorList(
        'random_graph',
        graph,
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
    node_color, edge_color = build_colors_list(case.graph)
    assert node_color == case.node_color and\
           edge_color == case.edge_color

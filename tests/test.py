import pytest

import networkx as nx

from .src.draw_graph import build_color_list
from .src.constants import Color, Attr


class CaseBuildColorList:
    
    def __init__(self, name: str, graph: nx.DiGraph,
                 node_color: List[str], edge_color: List[str]):
        self.name = name
        self.graph = graph
        self.node_color = node_color
        self.edge_color = edge_color

    def __str__(self) -> str:
        return 'test_{}'.format(self._name)


TEST_CASES_BUILD_COLOR_LIST = list()

TEST_CASES_BUILD_COLOR_LIST.append(
    CaseBuildColorList(
        'empty_graph',
        nx.DiGraph(),
        [],
        []
    )
)

graph = DiGraph()
graph.add_node('A', **{Attr.ColorAttr: Color.PROGRESS})
graph.add_node('B', **{Attr.ColorAttr: Color.REST})
graph.add_edge('A', 'B', **{Attr.ColorAttr: Color.PROGRESS})
graph.add_edge('A', 'C', **{Attr.ColorAttr: Color.REST})
node_color = [Color.PROGRESS.value, Color.REST.value, Color.REST.value]
edge_color = [Color.PROGRESS.value, Color.REST.value]

TEST_CASES_BUILD_COLOR_LIST.append(
    CaseBuildColorList(
        'random_graph',
        graph,
        node_color,
        edge_color
    )
)

@pytest.mark.parametrize('build_color_list', TEST_CASES_BUILD_COLOR_LIST, ids=str)
def test_build_color_list(case: CaseBuildColorList) -> None:
    node_color, edge_color = build_color_list(case.graph)
    assert all(node_color == case.node_color) and\
           all(edge_color == case.edge_color)

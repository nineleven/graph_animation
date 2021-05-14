import pytest

import networkx as nx

from src.render_graph import build_colors_list
from src.constants import Color

from typing import List, Any, Dict

from collections import defaultdict


class CaseBuildColorList:
    
    def __init__(self, name: str, graph: nx.DiGraph,
                 nodes_colors_dict: Dict[Any, Color],
                 edges_colors_dict: Dict[Any, Color],
                 node_color: List[str], edge_color: List[str]):
        self.name = name
        self.graph = graph
        self.nodes_colors_dict = nodes_colors_dict
        self.edges_colors_dict = edges_colors_dict
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


def default_func() -> Color:
    return Color.COLOR_REST


nodes_colors_dict = defaultdict(default_func)
edges_colors_dict = defaultdict(default_func)

graph = nx.DiGraph()
graph.add_node('A')
nodes_colors_dict['A'] = Color.COLOR_PROGRESS
graph.add_node('B')
nodes_colors_dict['B'] = Color.COLOR_REST
graph.add_edge('A', 'B')
edges_colors_dict[('A', 'B')] = Color.COLOR_PROGRESS
graph.add_edge('A', 'C')
edges_colors_dict[('A', 'C')] = Color.COLOR_REST
node_color = [Color.COLOR_PROGRESS.value, Color.COLOR_REST.value, Color.COLOR_REST.value]
edge_color = [Color.COLOR_PROGRESS.value, Color.COLOR_REST.value]

TEST_CASES_BUILD_COLOR_LIST.append(
    CaseBuildColorList(
        'random_graph',
        graph,
        nodes_colors_dict,
        edges_colors_dict,
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
    node_color, edge_color = build_colors_list(case.graph, case.nodes_colors_dict, case.edges_colors_dict)
    assert node_color == case.node_color and\
           edge_color == case.edge_color

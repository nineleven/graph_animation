import pytest

import networkx as nx

from itertools import zip_longest

from typing import Tuple, List, Iterator, Any

from src.constants import GraphElementType
from src.breadth_first_traversal import traversal as bf_trav
from src.depth_first_traversal import traversal as df_trav


class BaseCase:

    def __init__(self, name: str):
        self.name = name
    
    def __str__(self) -> str:
        return f'test_{self.name}'


class CaseExactTraversal(BaseCase):

    def __init__(self, name: str,
                 trav: Iterator[Tuple[GraphElementType, Any]],
                 answer: List[Tuple[GraphElementType, Any]]) -> None:
        super().__init__(name)
        
        self.trav = trav
        self.answer = answer
    

EXACT_TRAVERSAL_CASES = [
    CaseExactTraversal('LinkedList bf', bf_trav(nx.path_graph(4), 0),
                       [(GraphElementType.TYPE_NODE, 0),
                        (GraphElementType.TYPE_EDGE, (0, 1)),
                        (GraphElementType.TYPE_NODE, 1),
                        (GraphElementType.TYPE_EDGE, (1, 2)),
                        (GraphElementType.TYPE_NODE, 2),
                        (GraphElementType.TYPE_EDGE, (2, 3)),
                        (GraphElementType.TYPE_NODE, 3)
                        ]),
    CaseExactTraversal('LinkedList df',
                       df_trav(nx.path_graph(4), 0),
                       [(GraphElementType.TYPE_NODE, 0),
                        (GraphElementType.TYPE_EDGE, (0, 1)),
                        (GraphElementType.TYPE_NODE, 1),
                        (GraphElementType.TYPE_EDGE, (1, 2)),
                        (GraphElementType.TYPE_NODE, 2),
                        (GraphElementType.TYPE_EDGE, (2, 3)),
                        (GraphElementType.TYPE_NODE, 3)
                        ])
]


@pytest.mark.parametrize(
    'case',
    EXACT_TRAVERSAL_CASES,
    ids=str
)
def test_traversals(case: CaseExactTraversal) -> None:
    
    for output, answer in zip_longest(case.trav, case.answer):
        assert output == answer

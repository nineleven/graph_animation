import networkx as nx

from typing import Any, Deque, Iterator, Tuple

from collections import deque, defaultdict

from pathlib import Path

from .constants import GraphElementType
from .utils import get_logger


logger = get_logger(str(Path(__file__).name))


def traversal(graph: nx.DiGraph, start_node: Any) -> Iterator[Tuple[GraphElementType, Any]]:
    '''
    Breadth first graph traversal algoprithm
    
    Parameters
    ----------
    graph : networkx.DiGraph
        Graph
    start_node : Any
        A node to start from

    Yields
    ------
    Tuple[GraphElementType, Any]
        Tuple of type of the yielded graph element and the element itself
    '''

    visited_dict = defaultdict(bool)

    queue: Deque[Any] = deque()
    queue.append(start_node)

    visited_dict[start_node] = True

    while queue:
        curr_node = queue.popleft()
        yield GraphElementType.TYPE_NODE, curr_node

        for neighbor in graph[curr_node]:
            if not visited_dict[neighbor]:
                edge = (curr_node, neighbor)
                yield GraphElementType.TYPE_EDGE, edge
                
                queue.append(neighbor)
                visited_dict[neighbor] = True

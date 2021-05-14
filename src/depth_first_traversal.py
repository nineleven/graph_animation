import networkx as nx

from typing import Any, Tuple, Iterator

from collections import defaultdict

from .constants import GraphElementType


def traversal(graph: nx.DiGraph, start_node: Any) -> Iterator[Tuple[GraphElementType, Any]]:
    '''
    Deapth first graph traversal algoprithm
    
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

    def dfs(curr_node: Any) -> Iterator[Tuple[GraphElementType, Any]]:
        yield GraphElementType.TYPE_NODE, curr_node
        visited_dict[curr_node] = True

        for neighbor in graph[curr_node]:
            if not visited_dict[neighbor]:
                edge = (curr_node, neighbor)
                yield GraphElementType.TYPE_EDGE, edge
                
                yield from dfs(neighbor)
    
    yield from dfs(start_node)

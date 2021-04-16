import networkx as nx

import PIL

from typing import Any, List, DefaultDict

from collections import defaultdict

from .render_graph import render_graph
from .constants import GraphElementAttr, Color


def make_depth_first_search_frames(
        graph: nx.DiGraph, start_node: Any) -> List[PIL.Image.Image]:
    '''
    Creates a list of frames that constitute an animation of
    the depth first search in a graph.

    Parameters
    ----------
    graph : networkx.DiGraph
        Graph
    start_node : Any
        A node to start from

    Returns
    -------
    List[PIL.Image.Image]
        List of frames
    '''
    
    frames = []
    
    pos = nx.spring_layout(graph)

    def default_func() -> GraphElementAttr:
        return GraphElementAttr(Color.COLOR_REST, False)
    
    nodes_attr_dict: DefaultDict[Any, GraphElementAttr] = defaultdict(default_func)
    edges_attr_dict: DefaultDict[Any, GraphElementAttr] = defaultdict(default_func)
    
    def dfs(curr_node: Any) -> None:
        nodes_attr_dict[curr_node].marked = True
        nodes_attr_dict[curr_node].color = Color.COLOR_PROGRESS

        frames.append(render_graph(graph, nodes_attr_dict,
                                   edges_attr_dict, pos))

        for neighbor in graph[curr_node]:
            edge = (curr_node, neighbor)
            edges_attr_dict[edge].color = Color.COLOR_PROGRESS
            frames.append(render_graph(graph, nodes_attr_dict,
                                       edges_attr_dict, pos))

            if not nodes_attr_dict[neighbor].marked:
                dfs(neighbor)

            edges_attr_dict[(curr_node, neighbor)].color = Color.COLOR_REST
            frames.append(render_graph(graph, nodes_attr_dict,
                                       edges_attr_dict, pos))
    
        nodes_attr_dict[curr_node].color = Color.COLOR_REST
        frames.append(render_graph(graph, nodes_attr_dict,
                                   edges_attr_dict, pos))
    
    dfs(start_node)
    
    return frames

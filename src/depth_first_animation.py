import networkx as nx

import PIL

from typing import Any, List

from draw_graph import draw_graph
from constants import Attr, Color


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
    
    def rec(curr_node):
        graph.nodes[curr_node][Attr.ATTR_MARKED] = True
        graph.nodes[curr_node][Attr.ATTR_COLOR] = Color.COLOR_PROGRESS

        frames.append(draw_graph(graph, pos))

        for neighbor in graph[curr_node]:
            edge = (curr_node, neighbor)
            graph.edges[edge][Attr.ATTR_COLOR] = Color.COLOR_PROGRESS
            frames.append(draw_graph(graph, pos))

            if not graph.nodes[neighbor].get(Attr.ATTR_MARKED, False):
                rec(neighbor)

            del graph.edges[(curr_node, neighbor)][Attr.ATTR_COLOR]
            frames.append(draw_graph(graph, pos))
    
        del graph.nodes[curr_node][Attr.ATTR_COLOR]
        frames.append(draw_graph(graph, pos))
    
    rec(start_node)
    
    '''
    Cleaning up an attribute
    that was used to prevent
    algorithm from processing
    a node more than one time
    '''
    for node in graph.nodes:
        if Attr.MARKED_ATTR in graph.nodes[node]:
            del graph.nodes[node][Attr.ATTR_MARKED]
        
    return frames

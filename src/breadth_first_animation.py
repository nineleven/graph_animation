import networkx as nx

import PIL

from typing import Any, List, Deque

from .draw_graph import draw_graph
from .constants import Attr, Color

from collections import deque


def make_breadth_first_search_frames(
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

    queue: Deque[Any] = deque()
    queue.append(start_node)

    while queue:
        curr_node = queue.popleft()

        graph.nodes[curr_node][Attr.ATTR_MARKED] = True
        graph.nodes[curr_node][Attr.ATTR_COLOR] = Color.COLOR_PROGRESS
        frames.append(draw_graph(graph, pos))
        
        for neighbor in graph[curr_node]:
            
            if not graph.nodes[neighbor].get(Attr.ATTR_MARKED, False):
                edge = (curr_node, neighbor)
                graph.edges[edge][Attr.ATTR_COLOR] = Color.COLOR_PROGRESS
                frames.append(draw_graph(graph, pos))
                
                queue.append(neighbor)

    '''
    Removing the color attributes
    '''
    for node in graph.nodes:
        if Attr.ATTR_COLOR in graph.nodes[node]:
            del graph.nodes[node][Attr.ATTR_COLOR]
    for edge in graph.edges:
        if Attr.ATTR_COLOR in graph.edges[edge]:
            del graph.edges[edge][Attr.ATTR_COLOR]

    '''
    Cleaning up the attribute
    that was used to prevent
    algorithm from processing
    a node more than one time
    '''
    for node in graph.nodes:
        if Attr.ATTR_MARKED in graph.nodes[node]:
            del graph.nodes[node][Attr.ATTR_MARKED]
        
    return frames

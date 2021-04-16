import networkx as nx

import PIL

from typing import Any, List, Deque, DefaultDict

from .render_graph import render_graph
from .constants import GraphElementAttr, Color

from collections import deque, defaultdict


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

    def default_func() -> GraphElementAttr:
        return GraphElementAttr(Color.COLOR_REST, False)
    
    nodes_attr_dict: DefaultDict[Any, GraphElementAttr] = defaultdict(default_func)
    edges_attr_dict: DefaultDict[Any, GraphElementAttr] = defaultdict(default_func)

    while queue:
        curr_node = queue.popleft()

        nodes_attr_dict[curr_node].marked = True
        nodes_attr_dict[curr_node].color = Color.COLOR_PROGRESS
        frames.append(render_graph(graph, nodes_attr_dict,
                                   edges_attr_dict, pos))
        
        for neighbor in graph[curr_node]:
            
            if not nodes_attr_dict[neighbor].marked:
                edge = (curr_node, neighbor)
                edges_attr_dict[edge].color = Color.COLOR_PROGRESS
                frames.append(render_graph(graph, nodes_attr_dict,
                                           edges_attr_dict, pos))
                
                queue.append(neighbor)
   
    return frames

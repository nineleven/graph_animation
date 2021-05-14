import matplotlib.pyplot as plt
import PIL

from collections import defaultdict

import networkx as nx

from typing import List, Tuple, Dict, Any, Iterator

from pathlib import Path

from .constants import Color, GraphElementType
from .utils import figure_to_pil, get_logger


logger = get_logger(Path(__file__).name)


def build_colors_list(graph: nx.Graph,
                      nodes_colors_dict: Dict[Any, Color],
                      edges_colors_dict: Dict[Tuple, Color]) -> Tuple[List[str], List[str]]:
    '''
    Utility function used to determine
    colors of nodes and edges
    
    Parameters
    ----------
    graph : networkx.Graph
        Graph
    nodes_attr_dict : Dict[Any, Color]
        Dictionary that contains colors of all(!) nodes
    edges_attr_dict : Dict[Tuple, Color]
        Dictionary that contains colors of all(!) edges
    
    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple that contains two arrays of colors.
        One for nodes and the other for edges.
    '''

    node_colors = [nodes_colors_dict[node].value for node in graph.nodes]
    edge_colors = [edges_colors_dict[edge].value for edge in graph.edges]
        
    return node_colors, edge_colors


def render_graph(graph: nx.DiGraph,
                 nodes_colors_dict: Dict[Any, Color],
                 edges_colors_dict: Dict[Tuple, Color],
                 pos: dict) -> PIL.Image.Image:
    '''
    Creates image of a graph as an array of pixels
    
    Parameters
    ----------
    graph : networkx.DiGraph
        Graph
    nodes_attr_dict : Dict[Any, Color]
        Dictionary that contains colors of all(!) nodes
    edges_attr_dict : Dict[Tuple, Color]
        Dictionary that contains colors of all(!) edges
    pos : dict
        networkx graph layout
    
    Returns
    -------
    PIL.Image.Image
        Array of pixels
    '''
    node_colors, edge_colors = build_colors_list(graph, nodes_colors_dict, edges_colors_dict)
    
    fig = plt.figure()
    ax = plt.axes()
    
    nx.draw_networkx(
        graph,
        node_color=node_colors,
        edge_color=edge_colors,
        pos=pos,
        ax=ax
    )
    
    plt.close()
    
    return figure_to_pil(fig)


def make_traversal_frames(graph: nx.Graph, trav: Iterator[Tuple[GraphElementType, Any]]) -> List[PIL.Image.Image]:
    '''
    Creates a list of frames that constitute an animation of
    the given traversal in a graph.

    Parameters
    ----------
    graph : networkx.Graph
        Graph
    trav : Generator[Tuple[GraphElementType, Any]]
        Traversal generator that yields a tuple of (yielded graph element type, element itself)

    Returns
    -------
    List[PIL.Image.Image]
        List of frames
    '''
    
    frames = []
    
    pos = nx.spring_layout(graph)

    def default_func() -> Color:
        return Color.COLOR_REST
    
    nodes_colors_dict = defaultdict(default_func)
    edges_colors_dict = defaultdict(default_func)

    for elem_type, elem in trav:
        logger.debug((elem_type, elem))
        if elem_type == GraphElementType.TYPE_NODE:
            nodes_colors_dict[elem] = Color.COLOR_PROGRESS
            
        elif elem_type == GraphElementType.TYPE_EDGE:
            edges_colors_dict[elem] = Color.COLOR_PROGRESS
        else:
            raise ValueError('Unknown element type')

        frames.append(render_graph(graph, nodes_colors_dict,
                                   edges_colors_dict, pos))

    return frames

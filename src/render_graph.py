import matplotlib.pyplot as plt
import PIL

import networkx as nx

from typing import List, Tuple, Dict, Any

from .constants import GraphElementAttr
from .utils import figure_to_pil


def build_colors_list(graph: nx.Graph,
                      nodes_attr_dict: Dict[Any, GraphElementAttr],
                      edges_attr_dict: Dict[Tuple, GraphElementAttr]) -> Tuple[List[str], List[str]]:
    '''
    Utility function used to determine
    colors of nodes and edges
    
    Parameters
    ----------
    graph : networkx.Graph
        Graph
    nodes_attr_dict : Dict[Any, GraphElementAttr]
        Dictionary that contains constants.GraphElementAttr's of all(!) nodes
    edges_attr_dict : Dict[Tuple, GraphElementAttr]
        Dictionary that contains constants.GraphElementAttr's of all(!) edges
    
    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple that contains two arrays of colors.
        One for nodes and the other for edges.
    '''

    node_colors = [nodes_attr_dict[node].color.value for node in graph.nodes]
    edge_colors = [edges_attr_dict[edge].color.value for edge in graph.edges]
        
    return node_colors, edge_colors


def render_graph(graph: nx.DiGraph,
                 nodes_attr_dict: Dict[Any, GraphElementAttr],
                 edges_attr_dict: Dict[Tuple, GraphElementAttr],
                 pos: dict) -> PIL.Image.Image:
    '''
    Creates image of a graph as an array of pixels
    
    Parameters
    ----------
    graph : networkx.DiGraph
        Graph
    nodes_attr_dict : Dict[Any, GraphElementAttr]
        Dictionary that contains GraphElementAttr's of all(!) nodes
    edges_attr_dict : Dict[Tuple, GraphElementAttr]
        Dictionary that contains GraphElementAttr's of all(!) edges
    pos : dict
        networkx graph layout
    
    Returns
    -------
    PIL.Image.Image
        Array of pixels
    '''
    node_colors, edge_colors = build_colors_list(graph, nodes_attr_dict, edges_attr_dict)
    
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

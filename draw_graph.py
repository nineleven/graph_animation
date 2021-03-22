import matplotlib.pyplot as plt
import PIL

import networkx as nx

from typing import List, Tuple

from constants import Attr, Color
from utils import figure_to_pil


def build_colors_list(graph: nx.DiGraph) -> Tuple[List[Color], List[Color]]:
    '''
    Utility function used to determine
    colors of nodes and edges
    
    Parameters
    ----------
    graph : networkx.DiGraph
        Graph
    
    Returns
    -------
    Tuple[List[Color], List[Color]]
        A tuple that contains two arrays of colors.
        One for nodes and the other for edges.
    '''
    node_colors = []
    edge_colors = []
    
    for node in graph.nodes:
        color = graph.nodes[node].get(Attr.COLOR_ATTR, Color.COLOR_REST).value
        node_colors.append(color)
        
    for edge in graph.edges:
        color = graph.edges[edge].get(Attr.COLOR_ATTR, Color.COLOR_REST).value
        edge_colors.append(color)
        
    return node_colors, edge_colors


def draw_graph(graph: nx.DiGraph, pos: dict) -> PIL.Image.Image:
    '''
    Creates image of a graph as an array of pixels
    
    Parameters
    ----------
    graph : networkx.DiGraph
        Graph
    pos : dict
        networkx graph layout
    
    Returns
    -------
    PIL.Image.Image
        Array of pixels
    '''
    node_colors, edge_colors = build_colors_list(graph)
    
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

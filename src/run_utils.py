from typing import Tuple, Any

from pathlib import Path

import networkx as nx

import argparse

from .depth_first_traversal import traversal as df_trav
from .breadth_first_traversal import traversal as bf_trav
from .render_graph import make_traversal_frames
from .utils import make_animation, save_animation, get_logger


logger = get_logger(Path(__file__).name)


def parse_output_path() -> Tuple[str, Path, Any, Path]:
    parser = argparse.ArgumentParser()

    parser.add_argument('algorithm', metavar='algorithm', type=str,
                        nargs=1, help='algorithm to visualize (one of: depth_first, breadth_first)')
    parser.add_argument('input_path', metavar='input_path', type=str,
                        nargs=1, help='path to input graph file')
    parser.add_argument('start_node', metavar='start_node', type=str,
                        nargs=1, help='a node to start from')
    parser.add_argument('output_path', metavar='output_path', type=str,
                        nargs=1, help='path to output .gif file')

    args = parser.parse_args()

    algorithm = args.algorithm[0]
    input_path = Path(args.input_path[0])
    start_node = args.start_node[0]
    output_path = Path(args.output_path[0])

    assert algorithm in ['breadth_first', 'depth_first'], f'{algorithm} is not one of: breadth_first, depth_first'
    assert output_path.suffix == '.gif', 'Output file should have .gif extension'

    return algorithm, input_path, start_node, output_path


def rec_mkdir(path: Path) -> None:
    '''
    Recursively creates requered directory

    Parameters
    ----------
    path : pathlib.Path
        directory path
    '''
    if not path.exists():
        rec_mkdir(path.parent)
        path.mkdir()


def read_graph(input_path: Path) -> nx.DiGraph:
    return nx.read_edgelist(input_path, create_using=nx.DiGraph())


def make_anim_and_save(algorithm: str, graph: nx.DiGraph, start_node: Any, output_path: Path) -> None:

    if algorithm == 'depth_first':
        trav = df_trav(graph, start_node)
    elif algorithm == 'breadth_first':
        trav = bf_trav(graph, start_node)
    else:
        raise ValueError('Unknown algorithm:' + algorithm)

    frames = make_traversal_frames(graph, trav)

    logger.info(f'{len(frames)} frames')
    
    anim = make_animation(frames)

    save_animation(anim, str(output_path), fps=1)

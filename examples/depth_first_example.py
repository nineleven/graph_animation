import networkx as nx

from src.utils import make_animation, save_animation, rec_mkdir
from src.depth_first_animation import make_depth_first_search_frames

from example_utils import parse_output_path


def main() -> None:
    output_path = parse_output_path()
    output_dir = output_path.parent
    
    graph = nx.DiGraph()

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')
    graph.add_edge('D', 'E')
    graph.add_edge('A', 'E')
    graph.add_edge('B', 'D')
    graph.add_edge('D', 'F')

    frames = make_depth_first_search_frames(graph, 'A')
    anim = make_animation(frames)

    if not output_dir.exists():
        rec_mkdir(output_dir)

    save_animation(anim, str(output_path), fps=3)

    print('done')


if __name__ == '__main__':
    main()

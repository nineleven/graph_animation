import networkx as nx

from pathlib import Path

from utils import make_animation, save_animation
from depth_first_animation import make_depth_first_search_frames


def main() -> None:
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

    output_dir = Path('../output/')
    filename = 'animation.gif'

    if not output_dir.exists():
        '''
        recursively create
        required directory
        '''
        def rec_mkdir(path: Path) -> None:
            if not path.exists():
                rec_mkdir(path.parent)
                path.mkdir()

        rec_mkdir(output_dir)

    save_animation(anim, output_dir / filename, fps=3)


if __name__ == '__main__':
    main()

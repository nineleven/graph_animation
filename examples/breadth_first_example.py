import networkx as nx

from pathlib import Path

from .utils import make_animation, save_animation
from .breadth_first_animation import make_breadth_first_search_frames


def main() -> None:
    graph = nx.full_rary_tree(3, 10, nx.DiGraph())

    frames = make_breadth_first_search_frames(graph, 0)
    anim = make_animation(frames)

    output_dir = Path('../output/')
    filename = 'breadth_first.gif'

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

    save_animation(anim, str(output_dir / filename), fps=3)

    print('done')


if __name__ == '__main__':
    main()

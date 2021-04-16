import networkx as nx

from src.utils import make_animation, save_animation, rec_mkdir
from src.breadth_first_animation import make_breadth_first_search_frames

from example_utils import parse_output_path


def main() -> None:
    output_path = parse_output_path()
    output_dir = output_path.parent
    
    graph = nx.full_rary_tree(3, 10, nx.DiGraph())

    frames = make_breadth_first_search_frames(graph, 0)
    anim = make_animation(frames)

    if not output_dir.exists():
        rec_mkdir(output_dir)

    save_animation(anim, str(output_path), fps=3)

    print('done')


if __name__ == '__main__':
    main()

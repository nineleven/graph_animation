import networkx as nx

from utils import make_animation, save_animation
from depth_first_animation import make_depth_first_search_frames


def main():
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

    save_animation(anim, 'animation.gif', fps=3)


if __name__ == '__main__':
    main()

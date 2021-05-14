from pathlib import Path

from example_utils import parse_output_path, make_anim_and_save, \
    rec_mkdir, get_logger, read_graph


logger = get_logger(Path(__file__).name)


def main() -> None:
    algorithm, input_path, start_node, output_path = parse_output_path()
    
    output_dir = output_path.parent
    if not output_dir.exists():
        rec_mkdir(output_dir)

    graph = read_graph(input_path)

    assert start_node in graph.nodes, f'{start_node} is not a node'

    make_anim_and_save(algorithm, graph, start_node, output_path)

    logger.info('done')


if __name__ == '__main__':
    main()

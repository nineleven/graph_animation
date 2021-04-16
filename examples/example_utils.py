import argparse

from pathlib import Path


def parse_output_path() -> Path:
    parser = argparse.ArgumentParser()
    
    parser.add_argument('directory', metavar='dir', type=str,
                        nargs=1, help='output folder')
    parser.add_argument('filename', metavar='fn', type=str,
                        nargs=1, help='filename without extension')

    args = parser.parse_args()

    return Path(args.directory[0]) / (args.filename[0] + '.gif')

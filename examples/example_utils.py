import argparse

from pathlib import Path

import logging
import sys


def get_logger() -> logging.Logger:
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    stream_handler.setFormatter(formatter)
    
    logger.addHandler(stream_handler)

    return logger


def parse_output_path() -> Path:
    parser = argparse.ArgumentParser()
    
    parser.add_argument('directory', metavar='dir', type=str,
                        nargs=1, help='output folder')
    parser.add_argument('filename', metavar='fn', type=str,
                        nargs=1, help='filename without extension')

    args = parser.parse_args()

    return Path(args.directory[0]) / (args.filename[0] + '.gif')
    

from enum import Enum


class Color(Enum):
    COLOR_PROGRESS = 'green'
    COLOR_REST = 'red'


class GraphElementType(Enum):
    TYPE_NODE = 'node'
    TYPE_EDGE = 'edge'

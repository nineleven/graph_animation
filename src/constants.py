from enum import Enum
from dataclasses import dataclass


class Color(Enum):
    COLOR_PROGRESS = 'green'
    COLOR_REST = 'red'


@dataclass
class GraphElementAttr:
    color: Color
    marked: bool

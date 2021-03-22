from enum import Enum


class Color(Enum):
    COLOR_PROGRESS = 'green'
    COLOR_REST = 'red'


class Attr(Enum):
    ATTR_MARKED = '_anim_marked'
    ATTR_COLOR = '_anim_color'

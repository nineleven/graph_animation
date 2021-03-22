from enum import Enum

class Color(Enum):
    COLOR_PROGRESS = 'green'
    COLOR_REST = 'red'

class Attr(Enum):
    MARKED_ATTR = '_anim_marked'
    COLOR_ATTR = '_anim_color'

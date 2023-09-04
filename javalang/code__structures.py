from collections import namedtuple
from typing import NamedTuple


class Position(NamedTuple):
    line: int       # -1 end of line
    column: int     # -1 end of column
    idx: int


class TextRange(NamedTuple):
    start: Position
    stop: Position


# Position = namedtuple('Position', ['line', 'column', 'idx'])
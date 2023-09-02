import enum

__docformat__ = "restructuredtext"
"""
Documentation is located in docs/source/constants.rst
"""

# Main version
PYGAMELIB_VERSION = "1.3.0"

# Directions
NO_DIR = 10000000
UP = 10000001
DOWN = 10000010
LEFT = 10000011
RIGHT = 10000100
DRUP = 10000101
DRDOWN = 10000110
DLUP = 10000111
DLDOWN = 10001000

# Permissions
PLAYER_AUTHORIZED = 20000001
NPC_AUTHORIZED = 20000010
ALL_CHARACTERS_AUTHORIZED = 20000011
ALL_PLAYABLE_AUTHORIZED = ALL_CHARACTERS_AUTHORIZED
ALL_MOVABLE_AUTHORIZED = 20000100
NONE_AUTHORIZED = 20000101

# UI positions
ORIENTATION_HORIZONTAL = 30000001
ORIENTATION_VERTICAL = 30000010
ALIGN_LEFT = 30000011
ALIGN_RIGHT = 30000100
ALIGN_CENTER = 30000101

# Running states
RUNNING = 40000001
PAUSED = 40000010
STOPPED = 40000011


# Accepted input/validators
INTEGER_FILTER = 50000001
PRINTABLE_FILTER = 50000002

# Special constants
NO_PLAYER = 90000001
MODE_RT = 90000002
MODE_TBT = 90000003

# Path Finding Algorithm Constants
ALGO_BFS = 90000100
ALGO_ASTAR = 90000101

# Text styling constants
BOLD = "\x1b[1m"
UNDERLINE = "\x1b[4m"


class SizeConstraint(enum.IntEnum):
    # Use current height and width
    DEFAULT_SIZE = 60000001
    # Use minimum height and width
    MINIMUM_SIZE = 60000002
    # Use maximum height and width
    MAXIMUM_SIZE = 60000003
    # Use available space up to maximum height and width
    EXPAND = 60000004


class Alignment(enum.IntEnum):
    LEFT = 30000011
    RIGHT = 30000100
    CENTER = 30000101
    TOP = 30000110
    BOTTOM = 30000111
    V_CENTER = 30001000
    H_CENTER = 30001001


class Orientation(enum.IntEnum):
    HORIZONTAL = 30000001
    VERTICAL = 30000010


class InputValidator(enum.IntEnum):
    INTEGER_FILTER = 50000001
    PRINTABLE_FILTER = 50000002


class Direction(enum.IntEnum):
    # Directions
    NO_DIR = 10000000
    UP = 10000001
    DOWN = 10000010
    LEFT = 10000011
    RIGHT = 10000100
    DRUP = 10000101
    DRDOWN = 10000110
    DLUP = 10000111
    DLDOWN = 10001000

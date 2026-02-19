"""Game constants for the Snake game."""

from enum import Enum

# Grid dimensions (in cells)
DEFAULT_GRID_WIDTH = 20
DEFAULT_GRID_HEIGHT = 20
CELL_SIZE = 25

# Speed settings
DEFAULT_FPS = 8
SPEED_INCREMENT = 1
POINTS_PER_SPEED_INCREASE = 5
MAX_FPS = 25

# Window title
WINDOW_TITLE = "Snake Game"

# Retro Nokia-inspired color palette
BLACK = (0, 0, 0)
DARK_GREEN = (0, 80, 0)
GREEN = (0, 170, 0)
LIGHT_GREEN = (0, 220, 0)
RED = (200, 50, 50)
WHITE = (200, 200, 200)
GRAY = (80, 80, 80)


class Direction(Enum):
    """Cardinal directions for snake movement."""

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class GameState(Enum):
    """Possible states of the game."""

    PLAYING = "playing"
    GAME_OVER = "game_over"


# Opposite direction mapping to prevent 180° reversal.
OPPOSITE_DIRECTIONS: dict[Direction, Direction] = {
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP,
    Direction.LEFT: Direction.RIGHT,
    Direction.RIGHT: Direction.LEFT,
}

"""Snake model — pure data and movement logic, no rendering."""

from src.constants import Direction, OPPOSITE_DIRECTIONS


class Snake:
    """Represents the snake on the grid.

    The snake is a list of (x, y) cell coordinates. Index 0 is the head.
    """

    def __init__(self, start_x: int, start_y: int) -> None:
        """Initialize the snake at the given starting position.

        Args:
            start_x: Starting x cell coordinate.
            start_y: Starting y cell coordinate.
        """
        self.body: list[tuple[int, int]] = [(start_x, start_y)]
        self.direction = Direction.RIGHT
        self._grow_pending = False

    @property
    def head(self) -> tuple[int, int]:
        """Return the head position."""
        return self.body[0]

    def change_direction(self, new_direction: Direction) -> None:
        """Change direction, blocking 180° reversals.

        Args:
            new_direction: The requested new direction.
        """
        if OPPOSITE_DIRECTIONS.get(new_direction) != self.direction:
            self.direction = new_direction

    def move(self) -> None:
        """Advance the snake one cell in the current direction.

        If a growth is pending, the tail is not removed.
        """
        dx, dy = self.direction.value
        new_head = (self.head[0] + dx, self.head[1] + dy)
        self.body.insert(0, new_head)

        if self._grow_pending:
            self._grow_pending = False
        else:
            self.body.pop()

    def grow(self) -> None:
        """Schedule the snake to grow by one cell on the next move."""
        self._grow_pending = True

    def check_self_collision(self) -> bool:
        """Return True if the head overlaps any body segment."""
        return self.head in self.body[1:]

    def occupies(self, position: tuple[int, int]) -> bool:
        """Return True if the given position is occupied by the snake.

        Args:
            position: (x, y) cell coordinate to check.
        """
        return position in self.body

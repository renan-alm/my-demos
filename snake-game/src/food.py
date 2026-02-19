"""Food model — spawning logic, no rendering."""

import random


class Food:
    """Represents a food item on the grid."""

    def __init__(self) -> None:
        """Initialize food with no position until spawned."""
        self.position: tuple[int, int] = (0, 0)

    def spawn(
        self,
        grid_width: int,
        grid_height: int,
        occupied: set[tuple[int, int]],
    ) -> None:
        """Place food on a random unoccupied cell.

        Args:
            grid_width: Number of cells horizontally.
            grid_height: Number of cells vertically.
            occupied: Set of (x, y) cells currently occupied.
        """
        available = [
            (x, y)
            for x in range(grid_width)
            for y in range(grid_height)
            if (x, y) not in occupied
        ]

        if not available:
            # Grid is full — keep current position.
            return

        self.position = random.choice(available)

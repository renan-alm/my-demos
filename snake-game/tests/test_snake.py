"""Unit tests for the Snake model."""

from src.constants import Direction
from src.snake import Snake


class TestSnakeInitialization:
    """Tests for Snake initialization."""

    def test_starts_at_given_position(self) -> None:
        """Snake body should contain only the starting cell."""
        # Arrange & Act
        snake = Snake(5, 5)

        # Assert
        assert snake.body == [(5, 5)]
        assert snake.head == (5, 5)

    def test_initial_direction_is_right(self) -> None:
        """Snake should default to moving right."""
        # Arrange & Act
        snake = Snake(0, 0)

        # Assert
        assert snake.direction == Direction.RIGHT


class TestSnakeMovement:
    """Tests for Snake movement mechanics."""

    def test_move_right(self) -> None:
        """Snake should move one cell to the right."""
        # Arrange
        snake = Snake(5, 5)

        # Act
        snake.move()

        # Assert
        assert snake.head == (6, 5)

    def test_move_up(self) -> None:
        """Snake should move one cell upward."""
        # Arrange
        snake = Snake(5, 5)
        snake.direction = Direction.UP

        # Act
        snake.move()

        # Assert
        assert snake.head == (5, 4)

    def test_move_preserves_body_length_without_growth(self) -> None:
        """Body length stays 1 when no growth is pending."""
        # Arrange
        snake = Snake(5, 5)

        # Act
        snake.move()

        # Assert
        assert len(snake.body) == 1


class TestSnakeGrowth:
    """Tests for Snake growth after eating food."""

    def test_grow_increases_length_by_one(self) -> None:
        """After grow + move, body should be 2 cells."""
        # Arrange
        snake = Snake(5, 5)
        snake.grow()

        # Act
        snake.move()

        # Assert
        assert len(snake.body) == 2

    def test_grow_keeps_tail_in_place(self) -> None:
        """The old head becomes a body segment after growth."""
        # Arrange
        snake = Snake(5, 5)
        snake.grow()

        # Act
        snake.move()

        # Assert
        assert snake.body == [(6, 5), (5, 5)]


class TestSnakeDirectionChange:
    """Tests for direction change and 180° reversal guard."""

    def test_change_to_valid_direction(self) -> None:
        """Changing to a non-opposite direction should work."""
        # Arrange
        snake = Snake(5, 5)

        # Act
        snake.change_direction(Direction.UP)

        # Assert
        assert snake.direction == Direction.UP

    def test_block_180_reversal(self) -> None:
        """Changing to the opposite direction should be ignored."""
        # Arrange
        snake = Snake(5, 5)

        # Act — default is RIGHT, trying LEFT
        snake.change_direction(Direction.LEFT)

        # Assert
        assert snake.direction == Direction.RIGHT

    def test_allow_perpendicular_turn(self) -> None:
        """Turning 90° should always be allowed."""
        # Arrange
        snake = Snake(5, 5)
        snake.change_direction(Direction.UP)

        # Act
        snake.change_direction(Direction.LEFT)

        # Assert
        assert snake.direction == Direction.LEFT


class TestSnakeSelfCollision:
    """Tests for self-collision detection."""

    def test_no_collision_with_single_cell(self) -> None:
        """A single-cell snake cannot collide with itself."""
        # Arrange
        snake = Snake(5, 5)

        # Act & Assert
        assert snake.check_self_collision() is False

    def test_collision_when_head_overlaps_body(self) -> None:
        """Detect collision when the head revisits a body cell."""
        # Arrange — build a snake long enough to loop back
        snake = Snake(3, 0)
        snake.body = [(3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (1, 1)]
        snake.direction = Direction.DOWN

        # Act — move down then left to overlap (2, 0)
        snake.move()
        snake.change_direction(Direction.LEFT)
        snake.move()
        snake.change_direction(Direction.UP)
        snake.move()

        # Assert
        assert snake.check_self_collision() is True


class TestSnakeOccupies:
    """Tests for the occupies helper."""

    def test_occupies_head_position(self) -> None:
        """Should return True for the head cell."""
        # Arrange
        snake = Snake(3, 3)

        # Act & Assert
        assert snake.occupies((3, 3)) is True

    def test_does_not_occupy_empty_cell(self) -> None:
        """Should return False for a cell the snake is not on."""
        # Arrange
        snake = Snake(3, 3)

        # Act & Assert
        assert snake.occupies((0, 0)) is False

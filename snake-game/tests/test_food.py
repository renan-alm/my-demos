"""Unit tests for the Food model."""

from src.food import Food


class TestFoodSpawn:
    """Tests for food spawning logic."""

    def test_spawn_on_empty_grid(self) -> None:
        """Food should land on a valid cell within grid bounds."""
        # Arrange
        food = Food()

        # Act
        food.spawn(10, 10, occupied=set())

        # Assert
        x, y = food.position
        assert 0 <= x < 10
        assert 0 <= y < 10

    def test_spawn_avoids_occupied_cells(self) -> None:
        """Food must not spawn on an occupied cell."""
        # Arrange — occupy all cells except (0, 0)
        occupied = {(x, y) for x in range(5) for y in range(5)} - {(0, 0)}
        food = Food()

        # Act
        food.spawn(5, 5, occupied)

        # Assert
        assert food.position == (0, 0)

    def test_spawn_on_full_grid_keeps_position(self) -> None:
        """When no cells are available, position should not change."""
        # Arrange
        food = Food()
        food.position = (2, 2)
        occupied = {(x, y) for x in range(3) for y in range(3)}

        # Act
        food.spawn(3, 3, occupied)

        # Assert
        assert food.position == (2, 2)

    def test_spawn_deterministic_with_one_option(self) -> None:
        """When only one cell is free, food must land there."""
        # Arrange
        occupied = {(x, y) for x in range(3) for y in range(3)} - {(1, 2)}
        food = Food()

        # Act
        food.spawn(3, 3, occupied)

        # Assert
        assert food.position == (1, 2)

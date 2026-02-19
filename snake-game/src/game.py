"""Game engine — orchestrates game logic, no direct pygame calls."""

from src.constants import (
    DEFAULT_FPS,
    GameState,
    MAX_FPS,
    POINTS_PER_SPEED_INCREASE,
    SPEED_INCREMENT,
    Direction,
)
from src.food import Food
from src.snake import Snake


class Game:
    """Manages game state, collision detection, and score tracking."""

    def __init__(
        self,
        grid_width: int,
        grid_height: int,
        initial_fps: int = DEFAULT_FPS,
    ) -> None:
        """Initialize a new game.

        Args:
            grid_width: Number of cells horizontally.
            grid_height: Number of cells vertically.
            initial_fps: Starting frames per second.
        """
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.initial_fps = initial_fps
        self.reset()

    def reset(self) -> None:
        """Reset the game to its initial state."""
        center_x = self.grid_width // 2
        center_y = self.grid_height // 2
        self.snake = Snake(center_x, center_y)
        self.food = Food()
        self.score = 0
        self.state = GameState.PLAYING
        self.current_fps = self.initial_fps
        self._spawn_food()

    def handle_direction(self, direction: Direction) -> None:
        """Process a direction input from the player.

        Args:
            direction: The requested movement direction.
        """
        if self.state == GameState.PLAYING:
            self.snake.change_direction(direction)

    def tick(self) -> None:
        """Advance the game by one frame.

        Moves the snake, checks collisions, handles food consumption,
        and updates score and speed.
        """
        if self.state != GameState.PLAYING:
            return

        self.snake.move()

        if self._check_wall_collision() or self.snake.check_self_collision():
            self.state = GameState.GAME_OVER
            return

        if self.snake.head == self.food.position:
            self._consume_food()

    def _check_wall_collision(self) -> bool:
        """Return True if the snake head is outside the grid."""
        x, y = self.snake.head
        return x < 0 or x >= self.grid_width or y < 0 or y >= self.grid_height

    def _consume_food(self) -> None:
        """Handle the snake eating food: grow, score, speed up."""
        self.snake.grow()
        self.score += 1
        self._update_speed()
        self._spawn_food()

    def _update_speed(self) -> None:
        """Increase game speed every N points, up to a maximum."""
        target_fps = self.initial_fps + (
            (self.score // POINTS_PER_SPEED_INCREASE) * SPEED_INCREMENT
        )
        self.current_fps = min(target_fps, MAX_FPS)

    def _spawn_food(self) -> None:
        """Place food on a cell not occupied by the snake."""
        occupied = set(self.snake.body)
        self.food.spawn(self.grid_width, self.grid_height, occupied)

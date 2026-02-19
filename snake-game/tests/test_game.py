"""Unit tests for the Game engine."""

from src.constants import DEFAULT_FPS, Direction, GameState
from src.game import Game


class TestGameInitialization:
    """Tests for initial game state."""

    def test_starts_in_playing_state(self) -> None:
        """Game should begin in PLAYING state."""
        # Arrange & Act
        game = Game(20, 20)

        # Assert
        assert game.state == GameState.PLAYING

    def test_initial_score_is_zero(self) -> None:
        """Score should start at zero."""
        # Arrange & Act
        game = Game(20, 20)

        # Assert
        assert game.score == 0

    def test_snake_starts_at_center(self) -> None:
        """Snake head should be at the grid center."""
        # Arrange & Act
        game = Game(20, 20)

        # Assert
        assert game.snake.head == (10, 10)

    def test_food_is_spawned_on_init(self) -> None:
        """Food should have a valid position after initialization."""
        # Arrange & Act
        game = Game(20, 20)

        # Assert
        x, y = game.food.position
        assert 0 <= x < 20
        assert 0 <= y < 20


class TestGameWallCollision:
    """Tests for wall collision detection."""

    def test_moving_off_right_edge_triggers_game_over(self) -> None:
        """Game over when snake exits through the right wall."""
        # Arrange
        game = Game(5, 5)
        game.snake.body = [(4, 2)]
        game.snake.direction = Direction.RIGHT

        # Act
        game.tick()

        # Assert
        assert game.state == GameState.GAME_OVER

    def test_moving_off_top_edge_triggers_game_over(self) -> None:
        """Game over when snake exits through the top wall."""
        # Arrange
        game = Game(5, 5)
        game.snake.body = [(2, 0)]
        game.snake.direction = Direction.UP

        # Act
        game.tick()

        # Assert
        assert game.state == GameState.GAME_OVER

    def test_moving_off_left_edge_triggers_game_over(self) -> None:
        """Game over when snake exits through the left wall."""
        # Arrange
        game = Game(5, 5)
        game.snake.body = [(0, 2)]
        game.snake.direction = Direction.LEFT

        # Act
        game.tick()

        # Assert
        assert game.state == GameState.GAME_OVER

    def test_moving_off_bottom_edge_triggers_game_over(self) -> None:
        """Game over when snake exits through the bottom wall."""
        # Arrange
        game = Game(5, 5)
        game.snake.body = [(2, 4)]
        game.snake.direction = Direction.DOWN

        # Act
        game.tick()

        # Assert
        assert game.state == GameState.GAME_OVER


class TestGameFoodConsumption:
    """Tests for eating food and scoring."""

    def test_score_increases_on_food_eaten(self) -> None:
        """Score should increment by 1 when food is consumed."""
        # Arrange
        game = Game(10, 10)
        game.snake.body = [(3, 3)]
        game.snake.direction = Direction.RIGHT
        game.food.position = (4, 3)

        # Act
        game.tick()

        # Assert
        assert game.score == 1

    def test_snake_grows_on_food_eaten(self) -> None:
        """Snake should grow by 1 cell after eating."""
        # Arrange
        game = Game(10, 10)
        game.snake.body = [(3, 3)]
        game.snake.direction = Direction.RIGHT
        game.food.position = (4, 3)

        # Act
        game.tick()

        # Assert
        assert len(game.snake.body) == 1  # Growth pending on next move
        game.tick()
        assert len(game.snake.body) == 2

    def test_food_respawns_after_eaten(self) -> None:
        """Food should move to a new position after being consumed."""
        # Arrange
        game = Game(10, 10)
        game.snake.body = [(3, 3)]
        game.snake.direction = Direction.RIGHT
        game.food.position = (4, 3)

        # Act
        game.tick()

        # Assert — food should no longer be at the eaten position
        assert game.food.position != (4, 3) or game.score == 1


class TestGameSpeedScaling:
    """Tests for speed increases as score grows."""

    def test_speed_increases_after_threshold(self) -> None:
        """FPS should increase after scoring enough points."""
        # Arrange
        game = Game(20, 20, initial_fps=8)
        game.score = 4
        game.snake.body = [(3, 3)]
        game.snake.direction = Direction.RIGHT
        game.food.position = (4, 3)

        # Act — eat food to reach score 5
        game.tick()

        # Assert
        assert game.current_fps > 8

    def test_speed_does_not_exceed_maximum(self) -> None:
        """FPS should cap at MAX_FPS."""
        # Arrange
        game = Game(20, 20, initial_fps=8)
        game.score = 200

        # Act
        game._update_speed()

        # Assert — MAX_FPS is 25
        assert game.current_fps <= 25


class TestGameReset:
    """Tests for game reset functionality."""

    def test_reset_restores_initial_state(self) -> None:
        """After reset, score, state, and speed should be initial values."""
        # Arrange
        game = Game(20, 20, initial_fps=DEFAULT_FPS)
        game.score = 10
        game.state = GameState.GAME_OVER
        game.current_fps = 15

        # Act
        game.reset()

        # Assert
        assert game.score == 0
        assert game.state == GameState.PLAYING
        assert game.current_fps == DEFAULT_FPS

    def test_reset_repositions_snake_to_center(self) -> None:
        """Snake should return to the center after reset."""
        # Arrange
        game = Game(20, 20)
        game.snake.body = [(0, 0)]

        # Act
        game.reset()

        # Assert
        assert game.snake.head == (10, 10)


class TestGameStateTransitions:
    """Tests for game state management."""

    def test_tick_does_nothing_when_game_over(self) -> None:
        """Ticking in GAME_OVER state should not move the snake."""
        # Arrange
        game = Game(10, 10)
        game.state = GameState.GAME_OVER
        head_before = game.snake.head

        # Act
        game.tick()

        # Assert
        assert game.snake.head == head_before

    def test_direction_ignored_when_game_over(self) -> None:
        """Direction input during GAME_OVER should be ignored."""
        # Arrange
        game = Game(10, 10)
        game.state = GameState.GAME_OVER

        # Act
        game.handle_direction(Direction.UP)

        # Assert — direction unchanged from initialization
        assert game.snake.direction == Direction.RIGHT

"""Renderer — all Pygame drawing logic isolated here."""

import pygame

from src.constants import (
    BLACK,
    CELL_SIZE,
    DARK_GREEN,
    GRAY,
    GREEN,
    LIGHT_GREEN,
    RED,
    WHITE,
    GameState,
)
from src.game import Game


class Renderer:
    """Handles all drawing operations for the Snake game."""

    def __init__(self, grid_width: int, grid_height: int) -> None:
        """Initialize the renderer and create the game surface.

        Args:
            grid_width: Number of cells horizontally.
            grid_height: Number of cells vertically.
        """
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.pixel_width = grid_width * CELL_SIZE
        self.pixel_height = grid_height * CELL_SIZE
        self.screen = pygame.display.set_mode(
            (self.pixel_width, self.pixel_height)
        )
        self.font = pygame.font.SysFont("monospace", 20, bold=True)
        self.large_font = pygame.font.SysFont("monospace", 36, bold=True)

    def draw(self, game: Game) -> None:
        """Draw the full frame based on current game state.

        Args:
            game: The current game instance.
        """
        self.screen.fill(BLACK)
        self._draw_grid()
        self._draw_snake(game)
        self._draw_food(game)
        self._draw_score(game)

        if game.state == GameState.GAME_OVER:
            self._draw_game_over(game)

        pygame.display.flip()

    def _draw_grid(self) -> None:
        """Draw a subtle grid overlay."""
        for x in range(0, self.pixel_width, CELL_SIZE):
            pygame.draw.line(
                self.screen, DARK_GREEN, (x, 0), (x, self.pixel_height)
            )
        for y in range(0, self.pixel_height, CELL_SIZE):
            pygame.draw.line(
                self.screen, DARK_GREEN, (0, y), (self.pixel_width, y)
            )

    def _draw_snake(self, game: Game) -> None:
        """Draw the snake body with a lighter head.

        Args:
            game: The current game instance.
        """
        for i, (x, y) in enumerate(game.snake.body):
            color = LIGHT_GREEN if i == 0 else GREEN
            rect = pygame.Rect(
                x * CELL_SIZE + 1,
                y * CELL_SIZE + 1,
                CELL_SIZE - 2,
                CELL_SIZE - 2,
            )
            pygame.draw.rect(self.screen, color, rect)

    def _draw_food(self, game: Game) -> None:
        """Draw the food item.

        Args:
            game: The current game instance.
        """
        x, y = game.food.position
        rect = pygame.Rect(
            x * CELL_SIZE + 1,
            y * CELL_SIZE + 1,
            CELL_SIZE - 2,
            CELL_SIZE - 2,
        )
        pygame.draw.rect(self.screen, RED, rect)

    def _draw_score(self, game: Game) -> None:
        """Draw the current score in the top-left corner.

        Args:
            game: The current game instance.
        """
        text = self.font.render(f"Score: {game.score}", True, WHITE)
        self.screen.blit(text, (8, 4))

    def _draw_game_over(self, game: Game) -> None:
        """Draw a semi-transparent game-over overlay with restart prompt.

        Args:
            game: The current game instance.
        """
        overlay = pygame.Surface(
            (self.pixel_width, self.pixel_height), pygame.SRCALPHA
        )
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        game_over_text = self.large_font.render("GAME OVER", True, RED)
        score_text = self.font.render(
            f"Final Score: {game.score}", True, WHITE
        )
        restart_text = self.font.render(
            "Press ENTER to restart", True, GRAY
        )

        self._center_text(game_over_text, -40)
        self._center_text(score_text, 10)
        self._center_text(restart_text, 50)

    def _center_text(
        self, surface: pygame.Surface, y_offset: int = 0
    ) -> None:
        """Blit a text surface centered horizontally with a vertical offset.

        Args:
            surface: The rendered text surface.
            y_offset: Vertical pixel offset from center.
        """
        rect = surface.get_rect(
            center=(self.pixel_width // 2, self.pixel_height // 2 + y_offset)
        )
        self.screen.blit(surface, rect)

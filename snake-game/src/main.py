"""Main entry point — Pygame init, event loop, wiring Game + Renderer."""

import argparse
import sys

import pygame

from src.constants import (
    DEFAULT_FPS,
    DEFAULT_GRID_HEIGHT,
    DEFAULT_GRID_WIDTH,
    WINDOW_TITLE,
    Direction,
    GameState,
)
from src.game import Game
from src.renderer import Renderer

# Mapping from Pygame key constants to game directions.
KEY_DIRECTION_MAP: dict[int, Direction] = {
    pygame.K_UP: Direction.UP,
    pygame.K_DOWN: Direction.DOWN,
    pygame.K_LEFT: Direction.LEFT,
    pygame.K_RIGHT: Direction.RIGHT,
}


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for grid size and speed."""
    parser = argparse.ArgumentParser(
        description="Classic Nokia-style Snake game"
    )
    parser.add_argument(
        "--width",
        type=int,
        default=DEFAULT_GRID_WIDTH,
        help=f"Grid width in cells (default: {DEFAULT_GRID_WIDTH})",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=DEFAULT_GRID_HEIGHT,
        help=f"Grid height in cells (default: {DEFAULT_GRID_HEIGHT})",
    )
    parser.add_argument(
        "--speed",
        type=int,
        default=DEFAULT_FPS,
        help=f"Initial game speed / FPS (default: {DEFAULT_FPS})",
    )
    return parser.parse_args()


def run_game_loop(game: Game, renderer: Renderer) -> None:
    """Run the main game loop until the player quits.

    Args:
        game: The game engine instance.
        renderer: The renderer instance.
    """
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                # Restart on Enter during game over.
                if (
                    event.key == pygame.K_RETURN
                    and game.state == GameState.GAME_OVER
                ):
                    game.reset()
                    continue

                # Direction input during gameplay.
                direction = KEY_DIRECTION_MAP.get(event.key)
                if direction:
                    game.handle_direction(direction)

        game.tick()
        renderer.draw(game)
        clock.tick(game.current_fps)


def main() -> None:
    """Initialize Pygame and start the game."""
    args = parse_args()

    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)

    game = Game(args.width, args.height, args.speed)
    renderer = Renderer(args.width, args.height)

    try:
        run_game_loop(game, renderer)
    finally:
        pygame.quit()
        sys.exit(0)


if __name__ == "__main__":
    main()

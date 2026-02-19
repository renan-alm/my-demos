# Snake Game

Classic Nokia-style Snake game built with Python and Pygame.

## Prerequisites

- Python 3.12+
- pip

## Setup

```bash
cd snake-game
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python -m src.main [OPTIONS]
```

### Arguments

| Argument    | Type | Default | Description                  |
| ----------- | ---- | ------- | ---------------------------- |
| `--width`   | int  | 20      | Grid width in cells          |
| `--height`  | int  | 20      | Grid height in cells         |
| `--speed`   | int  | 8       | Initial game speed (FPS)     |

### Examples

```bash
# Default settings
python -m src.main

# Custom grid size and speed
python -m src.main --width 30 --height 25 --speed 10
```

## Controls

| Key          | Action        |
| ------------ | ------------- |
| Arrow keys   | Change direction |
| Enter        | Restart (game over screen) |
| Escape       | Quit          |

## Running Tests

```bash
pytest
```

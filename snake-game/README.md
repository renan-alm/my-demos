# Snake Game

A classic Snake game implementation in Python using Pygame, replicating the nostalgic snake game from old phones.

## Description

This is a faithful recreation of the classic Snake game that was popular on old mobile phones. Control the snake, eat food, grow longer, and try not to crash into yourself or the walls!

## Features

- Classic snake gameplay mechanics
- Grid-based movement
- Score tracking
- Game over detection with restart option
- Clean, retro-style graphics
- Smooth controls using arrow keys

## Requirements

- Python 3.7 or higher
- Pygame 2.5.2

## Installation

1. Navigate to the snake-game directory:
```bash
cd snake-game
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## How to Play

1. Run the game:
```bash
python snake_game.py
```

2. Use the arrow keys to control the snake:
   - **↑** Move up
   - **↓** Move down
   - **←** Move left
   - **→** Move right

3. Eat the red food to grow longer and increase your score.

4. Avoid hitting the walls or the snake's own body.

5. When game is over:
   - Press **SPACE** to restart
   - Press **ESC** to quit

## Game Rules

- The snake starts with a length of 3 segments
- Each food eaten increases the score by 10 points
- The snake grows by one segment each time it eats food
- The game ends if the snake hits a wall or itself
- You cannot reverse direction (e.g., can't go left if moving right)

## Controls

- **Arrow Keys**: Move the snake
- **ESC**: Quit the game
- **SPACE**: Restart after game over

## Configuration

You can modify the game settings by changing the parameters when creating the game:

```python
game = SnakeGame(width=600, height=600, grid_size=20)
```

- `width`: Window width in pixels (default: 600)
- `height`: Window height in pixels (default: 600)
- `grid_size`: Size of each grid cell in pixels (default: 20)

## Screenshot

The game features:
- A 30x30 grid (600x600 pixels with 20px cells)
- Green snake with darker head
- Red food
- Black background with dark gray grid lines
- Score display in the top-left corner

Enjoy the nostalgia!

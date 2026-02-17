import pygame
import random
import sys
from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class SnakeGame:
    def __init__(self, width=600, height=600, grid_size=20):
        """
        Initialize the Snake game.
        
        Args:
            width: Window width in pixels (default: 600)
            height: Window height in pixels (default: 600)
            grid_size: Size of each grid cell in pixels (default: 20)
        """
        pygame.init()
        
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.grid_width = width // grid_size
        self.grid_height = height // grid_size
        
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Snake Game')
        
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        self.colors = {
            'background': (0, 0, 0),
            'snake': (0, 255, 0),
            'snake_head': (0, 200, 0),
            'food': (255, 0, 0),
            'text': (255, 255, 255),
            'grid': (40, 40, 40)
        }
        
        self.reset_game()
    
    def reset_game(self):
        start_x = self.grid_width // 2
        start_y = self.grid_height // 2
        
        self.snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
    
    def generate_food(self):
        while True:
            food = (random.randint(0, self.grid_width - 1), random.randint(0, self.grid_height - 1))
            if food not in self.snake:
                return food
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                    elif event.key == pygame.K_ESCAPE:
                        return False
                else:
                    if event.key == pygame.K_UP and self.direction != Direction.DOWN:
                        self.next_direction = Direction.UP
                    elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                        self.next_direction = Direction.DOWN
                    elif event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                        self.next_direction = Direction.LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                        self.next_direction = Direction.RIGHT
                    elif event.key == pygame.K_ESCAPE:
                        return False
        
        return True
    
    def update(self):
        if self.game_over:
            return
        
        self.direction = self.next_direction
        
        head_x, head_y = self.snake[0]
        
        if self.direction == Direction.UP:
            new_head = (head_x, head_y - 1)
        elif self.direction == Direction.DOWN:
            new_head = (head_x, head_y + 1)
        elif self.direction == Direction.LEFT:
            new_head = (head_x - 1, head_y)
        else:
            new_head = (head_x + 1, head_y)
        
        if (new_head[0] < 0 or new_head[0] >= self.grid_width or
            new_head[1] < 0 or new_head[1] >= self.grid_height or
            new_head in self.snake):
            self.game_over = True
            return
        
        self.snake.insert(0, new_head)
        
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
        else:
            self.snake.pop()
    
    def draw(self):
        self.screen.fill(self.colors['background'])
        
        for x in range(0, self.width, self.grid_size):
            pygame.draw.line(self.screen, self.colors['grid'], (x, 0), (x, self.height))
        for y in range(0, self.height, self.grid_size):
            pygame.draw.line(self.screen, self.colors['grid'], (0, y), (self.width, y))
        
        for i, (x, y) in enumerate(self.snake):
            color = self.colors['snake_head'] if i == 0 else self.colors['snake']
            pygame.draw.rect(
                self.screen,
                color,
                (x * self.grid_size, y * self.grid_size, self.grid_size, self.grid_size)
            )
        
        food_x, food_y = self.food
        pygame.draw.rect(
            self.screen,
            self.colors['food'],
            (food_x * self.grid_size, food_y * self.grid_size, self.grid_size, self.grid_size)
        )
        
        score_text = self.small_font.render(f'Score: {self.score}', True, self.colors['text'])
        self.screen.blit(score_text, (10, 10))
        
        if self.game_over:
            game_over_text = self.font.render('GAME OVER!', True, self.colors['text'])
            final_score_text = self.font.render(f'Final Score: {self.score}', True, self.colors['text'])
            restart_text = self.small_font.render('Press SPACE to restart or ESC to quit', True, self.colors['text'])
            
            text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2 - 50))
            score_rect = final_score_text.get_rect(center=(self.width // 2, self.height // 2))
            restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
            
            self.screen.blit(game_over_text, text_rect)
            self.screen.blit(final_score_text, score_rect)
            self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def run(self):
        running = True
        
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(10)
        
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = SnakeGame()
    game.run()

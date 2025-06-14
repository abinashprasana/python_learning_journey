"""
Simple Snake Game
Author: Abinash Prasana

A beginner-friendly version of the classic Snake game using pygame.
Use arrow keys to move. Eat food to grow. Avoid crashing into walls or yourself.
"""

import pygame
import random

# Initialize pygame
pygame.init()

# Set up game window
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Abby's Simple Snake")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Draw snake blocks
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# Display message
def show_message(text):
    msg = font.render(text, True, RED)
    screen.blit(msg, [WIDTH // 6, HEIGHT // 2])

# Main function
def game_loop():
    game_over = False
    x = WIDTH // 2
    y = HEIGHT // 2
    dx, dy = 0, 0

    snake = []
    length = 1

    # Generate food
    food_x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    food_y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, BLOCK_SIZE

        x += dx
        y += dy

        # Check collision with wall
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True

        # Update snake
        head = [x, y]
        snake.append(head)
        if len(snake) > length:
            del snake[0]

        # Check self-collision
        for segment in snake[:-1]:
            if segment == head:
                game_over = True

        # Check food collision
        if x == food_x and y == food_y:
            length += 1
            food_x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            food_y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

        # Drawing
        screen.fill(BLACK)
        draw_snake(snake)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        pygame.display.update()
        clock.tick(10)  # Speed

    screen.fill(BLACK)
    show_message("Game Over! Close the window to exit.")
    pygame.display.update()
    pygame.time.wait(2000)

    pygame.quit()

# Run the game
game_loop()
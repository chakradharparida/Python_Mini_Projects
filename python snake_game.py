import pygame
import time
import random

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
screen_width = 800
screen_height = 600

# Create game screen
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Clock and speed
clock = pygame.time.Clock()
snake_speed = 15

# Snake block size
block_size = 10

# Font for displaying score
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the score
def display_score(score):
    value = score_font.render(f"Score: {score}", True, blue)
    game_screen.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_screen, black, [x[0], x[1], block_size, block_size])

# Function for the message when the game ends
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_screen.blit(mesg, [screen_width / 6, screen_height / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Snake movement direction
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_screen.fill(white)
            message("You Lost! Press C to Play Again or Q to Quit", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_screen.fill(white)
        pygame.draw.rect(game_screen, green, [food_x, food_y, block_size, block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()

import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20

GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

FPS = 120

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def draw_grid(positions):
    screen.fill(BLACK)

    for position in positions:
        column, row = position
        top_left = (column * TILE_SIZE, row * TILE_SIZE)

        pygame.draw.rect(screen, WHITE, (*top_left, TILE_SIZE, TILE_SIZE))

    for x in range(GRID_WIDTH):
        pygame.draw.line(screen, GREY, (x * TILE_SIZE, 0), (x * TILE_SIZE, HEIGHT))

    for y in range(GRID_HEIGHT):
        pygame.draw.line(screen, GREY, (0, y * TILE_SIZE), (WIDTH, y * TILE_SIZE))

def main_loop():
    running = True
    playing = False

    positions = set()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                column = x // TILE_SIZE
                row = y // TILE_SIZE

                position = (column, row)

                if position in positions:
                    positions.remove(position)
                else:
                    positions.add(position)

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:
                    positions = set()
                    playing = False

                if event.key == pygame.K_r:
                    num_positions = random.randrange(4, 10) * GRID_WIDTH
                    positions = set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for _ in range(num_positions)])

        draw_grid(positions)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main_loop()
import pygame

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

    positions = set()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_grid(positions)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main_loop()
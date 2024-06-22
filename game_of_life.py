import pygame

pygame.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20

GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

FPS = 120

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def main_loop():
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main_loop()
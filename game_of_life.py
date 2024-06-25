import time
import pygame
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 10

GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

def gameoflife():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Conway\'s Game of Life')

    cells = np.zeros((GRID_WIDTH, GRID_HEIGHT))

    screen.fill(BLACK)
    
    update_cells(screen, cells)

    pygame.display.flip()
    pygame.display.update()

    playing = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                    update_cells(screen, cells)
                    pygame.display.update()
            
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()

                column = x // TILE_SIZE
                row = y // TILE_SIZE

                cells[row, column] = 1

                update_cells(screen, cells)
                pygame.display.update()

        screen.fill(BLACK)

        if playing:
            cells = update_cells(screen, cells, playing=True)
            pygame.display.update()

        time.sleep(0.001)

def update_cells(screen, current_generation, playing=False):
    next_generation = np.zeros((current_generation.shape[0], current_generation.shape[1]))

    for row, column in np.ndindex(current_generation.shape):
        alive = np.sum(current_generation[row-1:row+2, column-1:column+2]) - current_generation[row, column]
        color = BLACK if (current_generation[row, column] == 0) else WHITE

        if current_generation[row, column] == 1:
            if (2 <= alive <= 3):
                next_generation[row, column] = 1
                if playing:
                    color = WHITE
        else:
            if (alive == 3):
                next_generation[row, column] = 1
                if playing:
                    color = WHITE

        pygame.draw.rect(screen, color, (column * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    return next_generation

if __name__ == "__main__":
    gameoflife()
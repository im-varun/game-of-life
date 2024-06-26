import time
import pygame
import numpy as np

# RGB values for colors to be used
BLACK = (0, 0, 0)
LIGHT_BLACK = (40, 40, 40)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

# display screen width and height (in pixels)
WIDTH, HEIGHT = 800, 800

# size of a cell (in pixels)
CELL_SIZE = 10

# calculate and store grid's width and height (in pixels)
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

def gameoflife():
    '''
    This is the main entry point for Conway's Game of Life and contains the loop
    for the simulation.
    '''

    # initialize all imported pygame modules
    pygame.init()

    # initialize a screen for display and set screen caption
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Conway\'s Game of Life')

    # numpy array of (GRID_WIDTH, GRID_HEIGHT) shape to store cell states (0 for dead and 1 for alive)
    # initialized with all zeros to indicate all cells are dead initially
    cells = np.zeros((GRID_WIDTH, GRID_HEIGHT))

    # fill screen with LIGHT_BLACK color
    screen.fill(LIGHT_BLACK)
    
    # update grid of cells
    update_cells(screen, cells)

    # update full display screen and portions of the screen for software displays
    pygame.display.flip()
    pygame.display.update()

    # variable to check if game is in progress or is paused by the user
    playing = False

    # loop for the Game of Life simulation
    while True:
        for event in pygame.event.get():
            # if user clicked X on the screen window or pressed Escape key, quit the game
            if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                # if the user pressed Spacebar key, continue or pause the game based on its current state
                if event.key == pygame.K_SPACE:
                    playing = not playing

                # if the user pressed r key, generate a grid of cells with random states (alive or dead)
                if event.key == pygame.K_r:
                    cells = np.random.choice([0, 1], (GRID_WIDTH, GRID_HEIGHT), p=[0.9, 0.1])

                # if the user pressed c key, clear the current grid of cells on the screen
                if event.key == pygame.K_c:
                    cells = np.zeros((GRID_WIDTH, GRID_HEIGHT))

                update_cells(screen, cells)
                pygame.display.update()
            
            # if the user pressed left mouse on the screen, toggle cell state at that mouse location
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()

                if (0 <= x < WIDTH) and (0 <= y < HEIGHT):
                    column = x // CELL_SIZE
                    row = y // CELL_SIZE

                    cells[row, column] = 1

                    update_cells(screen, cells)
                    pygame.display.flip()

        # fill screen with LIGHT_BLACK color
        screen.fill(LIGHT_BLACK)

        # if the game is in progress, update cells array and update screen display
        if playing:
            cells = update_cells(screen, cells, playing=True)
            pygame.display.update()

        # create a 0.0001 second delay
        time.sleep(0.001)

def update_cells(screen, current_generation, playing=False):
    '''
    This is used to update the grid of cells.

    :param screen: Pygame screen on which cells are drawn.
    :param current_generation: Numpy array containing cells states for current generation.
    :param playing: Boolean variable to indicate if game is in progress or is paused by the user (default=False).
    '''

    # numpy array of (GRID_WIDTH, GRID_HEIGHT) shape to store cell states for next generation
    next_generation = np.zeros((current_generation.shape[0], current_generation.shape[1]))

    # iterate through cell states in current generation
    for row, column in np.ndindex(current_generation.shape):
        # calculate total alive neighbors of the current cell
        alive = np.sum(current_generation[row-1:row+2, column-1:column+2]) - current_generation[row, column]
        
        # color to display for the current cell based on its state
        color = BLACK if (current_generation[row, column] == 0) else WHITE

        # check current cell state and its total alive neighbors
        # according to game rules, change current cell state for next generation and set cell color to display
        if current_generation[row, column] == 1:
            if (alive < 2) or (alive > 3):
                if playing:
                    color = GREY
            elif (2 <= alive <= 3):
                next_generation[row, column] = 1
                if playing:
                    color = WHITE
        else:
            if (alive == 3):
                next_generation[row, column] = 1
                if playing:
                    color = WHITE

        # draw current cell on the screen
        pygame.draw.rect(screen, color, (column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # return numpy array of cell states for next generation
    return next_generation

if __name__ == "__main__":
    gameoflife()
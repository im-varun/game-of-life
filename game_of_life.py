import pygame

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 10

GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

FPS = 60

def draw_grid(screen, positions):
    screen.fill(BLACK)

    for position in positions:
        column, row = position
        top_left = (column * TILE_SIZE, row * TILE_SIZE)

        pygame.draw.rect(screen, WHITE, (*top_left, TILE_SIZE, TILE_SIZE))

    for x in range(GRID_WIDTH):
        pygame.draw.line(screen, GREY, (x * TILE_SIZE, 0), (x * TILE_SIZE, HEIGHT))

    for y in range(GRID_HEIGHT):
        pygame.draw.line(screen, GREY, (0, y * TILE_SIZE), (WIDTH, y * TILE_SIZE))

def update_cells(positions):
    all_neighbors = set()

    new_positions = set()

    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors)

        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) in [2, 3]:
            new_positions.add(position)

    for position in all_neighbors:
        neighbors = get_neighbors(position)
        neighbors = list(filter(lambda x: x in position, neighbors))

        if len(neighbors) == 3:
            new_positions.add(position)

    return new_positions

def get_neighbors(position):
    x, y = position

    neighbors = list()

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx == 0) or (dy == 0):
                continue

            nx, ny = x + dx, y + dy

            if ((nx >= 0) and (nx < GRID_WIDTH)) and ((ny >= 0) and (ny < GRID_HEIGHT)):
                neighbors.append((nx, ny))

    return neighbors

def main_loop():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    playing = False
    count = 0
    update_freq = 10

    positions = set()

    while running:
        clock.tick(FPS)

        if playing:
            count += 1

        if count >= update_freq:
            count = 0
            positions = update_cells(positions)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:
                    positions = set()
                    playing = False
                    count = 0

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()

                column = x // TILE_SIZE
                row = y // TILE_SIZE

                position = (column, row)

                if position in positions:
                    positions.remove(position)
                else:
                    positions.add(position)

        draw_grid(screen, positions)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main_loop()
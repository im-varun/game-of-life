# Conway's Game of Life

This project is a simple 2D implementation of Conway's Game of Life in Python, using [pygame](https://www.pygame.org/news) and [numpy](https://numpy.org/) libraries.  

# About Game of Life

The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.  

**Rules**
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.  
2. Any live cell with two or three live neighbours lives on to the next generation.  
3. Any live cell with more than three live neighbours dies, as if by overpopulation.  
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.  

# Installation

Prerequisite: A latest version of [Python](https://www.python.org/)

To install and run Conway's Game of Life, follow these steps:

1. Clone the repository:
```sh
git clone https://github.com/im-varun/game-of-life.git
```

2. Navigate to the project directory:
```sh
cd game-of-life
```

3. Install the required dependencies:
```sh
pip install -r requirements.txt
```

4. Run the Game of Life simulation:
```sh
python game_of_life.py
```

# Usage

The Game of Life simulation uses the following controls:
1. Toggle cell state: `Left Mouse Button`
2. Start/Stop the simulation: `Spacebar`
3. Generate random cells on the grid: `r`
4. Clear the cells on the grid: `c`
5. Quit: `Esc` (alternatively, use the X button on the screen)

# Demo

[Game of Life Demo](https://drive.google.com/file/d/1lrzkJhhzoWIpc4yJLre5lUxwpApZLALX/view?usp=sharing)
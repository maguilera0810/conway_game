import pygame
from pygame.locals import *
import sys
from random import *
import time
# import juegovida as jv
# ------constantes

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
color_muerto = [0, 0, 0]
color_vivo1 = [255, 0, 255]
color_vivo2 = [0, 255, 255]


# Create a grid with a Glider pattern
randon = 0


def checkCell(row, col, grid, gridSize, mini, maxi, dife):
    # We will count neighbours except when at the edge of the grid
    minRow = 0
    if row > 1:
        minRow = row-1
    maxRow = gridSize-1
    if row < gridSize-2:
        maxRow = row+1
    minCol = 0
    if col > 1:
        minCol = col-1
    maxCol = gridSize-1
    if col < gridSize-2:
        maxCol = col+1

    # Count the number of neighbours
    neighbours1 = 0
    neighbours2 = 0
    for nrow in range(minRow, maxRow+1):
        for ncol in range(minCol, maxCol+1):
            if grid[nrow][ncol] == 1:
                neighbours1 += 1
            elif grid[nrow][ncol] == 2:
                neighbours2 += 1
    dife_v=abs(neighbours1-neighbours2)
    tipo = randint(0,1)
    if tipo:
        # Apply the four key rules of Conway's Game of Life
        # 11111111111111111111111111111111
        if grid[row][col] == 1:
            # 1.Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
            # 3.Any live cell with more than three live neighbours dies, as if by overpopulation.
            # 2.Any live cell with two or three live neighbours lives on to the next generation.
            # 4.Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            if neighbours1 < mini or (neighbours1 + neighbours2) > maxi:
                return 0
            elif (mini <= (neighbours2+neighbours1) <= maxi):
                if neighbours1 < neighbours2:
                    if dife_v>=dife:
                        return 2
                    else:
                        return 1
                elif neighbours1 > neighbours2:
                    if dife_v>=dife:
                        return 1
                    else:
                        return 2
                else:
                    return 1    
            else:
                return 0
        elif grid[nrow][ncol] == 2:
            if neighbours2 < mini or (neighbours1 + neighbours2) > maxi:
                return 0
            elif (mini <= (neighbours2+neighbours1) <= maxi):
                if neighbours1 < neighbours2:
                    if dife_v>=dife:
                        return 2
                    else:
                        return 1
                elif neighbours1 > neighbours2:
                    if dife_v>=dife:
                        return 1
                    else:
                        return 2
                else:
                    return 2    
            else:
                return 0
        else:
            if (mini <= (neighbours2+neighbours1) <= maxi):
                if neighbours1 < neighbours2:
                    if dife_v>=dife:
                        return 2
                    else:
                        return 0
                elif neighbours1 > neighbours2:
                    if dife_v>=dife:
                        return 1
                    else:
                        return 0
                else:
                    return 0
    elif not tipo:
        if grid[nrow][ncol] == 2:
            if neighbours2 < mini or (neighbours1 + neighbours2) > maxi:
                return 0
            elif (mini <= (neighbours2+neighbours1) <= maxi):
                if neighbours1 < neighbours2:
                    if dife_v>=dife:
                        return 2
                    else:
                        return 1
                elif neighbours1 > neighbours2:
                    if dife_v>=dife:
                        return 1
                    else:
                        return 2
                else:
                    return 2    
            else:
                return 0
        elif grid[row][col] == 1:
            if neighbours1 < mini or (neighbours1 + neighbours2) > maxi:
                return 0
            elif (mini <= (neighbours2+neighbours1) <= maxi):
                if neighbours1 < neighbours2:
                    if dife_v>=dife:
                        return 2
                    else:
                        return 1
                elif neighbours1 > neighbours2:
                    if dife_v>=dife:
                        return 1
                    else:
                        return 2
                else:
                    return 1    
            else:
                return 0
        else:
            if (mini <= (neighbours2+neighbours1) <= maxi):
                if neighbours1 < neighbours2:
                    if dife_v>=dife:
                        return 2
                    else:
                        return 0
                elif neighbours1 > neighbours2:
                    if dife_v>=dife:
                        return 1
                    else:
                        return 0
                else:
                    return 0




def randomGrid(gridSize):
    grid = []
    for row in range(0, gridSize):
        grid.append([])
        for col in range(0, gridSize):
            pos = randint(0,2)
            grid[row].append(pos)

    return grid


def mitGrid(gridSize):
    grid = []
    for row in range(0, gridSize):
        grid.append([])
        for col in range(0, gridSize):
            if row<gridSize//2:
                pos = randint(0,1)
            else:
                pos = randint(0,1)
                if pos:
                    pos=2
            grid[row].append(pos)

    return grid

def tetra_Grid(gridSize):
    grid = []
    for row in range(0, gridSize):
        grid.append([])
        for col in range(0, gridSize):
            if row<gridSize//2 and col <gridSize//2:
                pos = randint(0,1)
            elif row<gridSize//2 and col >=gridSize//2:
                pos = randint(0,1)
                if pos:
                    pos=2
            elif row>=gridSize//2 and col >=gridSize//2:
                pos = randint(0,1)
            elif row>=gridSize//2 and col <gridSize//2:
                pos = randint(0,1)
                if pos:
                    pos=2
            grid[row].append(pos)

    return grid

def multi_Grid(gridSize):
    grid = []
    for row in range(0, gridSize):
        grid.append([])
        for col in range(0, gridSize):
            if row<gridSize//2 and col <gridSize//2:
                pos = randint(0,1)
            elif row<gridSize//2 and col >=gridSize//2:
                pos = randint(0,1)
                if pos:
                    pos=2
            elif row>=gridSize//2 and col >=gridSize//2:
                pos = randint(0,1)
            elif row>=gridSize//2 and col <gridSize//2:
                pos = randint(0,1)
                if pos:
                    pos=2
            grid[row].append(pos)

    return grid


# -----------graficos
def drawn_box(screen, px, py, size=50, color=color_muerto, width=0):
    rect = (px, py, size, size)
    pygame.draw.rect(screen, color, rect, width)


def drawn_Grid(screen, grid, px, py, size=50):
    pos_x = px
    pos_y = py
    i = 0
    while i < len(grid):
        pos_y = py+size*i
        j = 0
        while j < len(grid[0]):
            pos_x = px+size*j
            if grid[i][j] == 1:
                drawn_box(screen, pos_x, pos_y, size, color_vivo1, 1)
            elif grid[i][j] == 2:
                drawn_box(screen, pos_x, pos_y, size, color_vivo2, 1)
            else:
                drawn_box(screen, pos_x, pos_y, size, color_muerto)
            j += 1
        i += 1


def main():
    pygame.init()
    GRID1 = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
    GRID = [
        [1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1]]
    GRID = [[1, 0], [0, 1]]
    # GRID=[[1]]

    top_left = 0
    top_righ = 0
    slip = 1
    mini = 3
    maxi = 6
    size = 10
    gridSize = 100
    #currentgrid = randomGrid(gridSize)
    #currentgrid = mitGrid(gridSize)
    currentgrid = tetra_Grid(gridSize)

    nextgrid = []
    for row in range(gridSize):
        nextgrid.append([])
        for col in range(gridSize):
            nextgrid[row].append(0)

    # creamos la ventana y le indicamos un titulo:
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen = pygame.display.set_mode((gridSize*size, gridSize*size))
    pygame.display.set_caption("Juego de la vida")
    # el bucle principal del juego
    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill([0, 0, 0])
        drawn_Grid(screen, currentgrid, top_left, top_righ, size)
        pygame.display.flip()
        if slip:
            time.sleep(0.5)

    # Generate Next Grid using the four key rules of Conway's Game of Life
        for row in range(gridSize):
            for col in range(gridSize):
                nextgrid[row][col] = checkCell(
                    row, col, currentgrid, gridSize, mini, maxi,1)
        # Swap grids (nextgrid becomes currentgrid)
        tmpgrid = currentgrid
        currentgrid = nextgrid
        nextgrid = tmpgrid

        # drawn_box(screen,100,100,100,100)


if __name__ == "__main__":
    main()

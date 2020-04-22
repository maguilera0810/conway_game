import pygame
from pygame.locals import *
import sys
from random import *
import time
#import juegovida as jv
#------constantes

RANDON = True

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
color_vivo1 = [0, 0, 0]
color_muerto1 = [0, 255, 255]
color_vivo2 = [0, 255, 255]
color_muerto2 = [0, 0, 0]

color_vivo=color_vivo2
color_muerto=color_muerto2

def checkCell(row, col, grid,gridSize,mini,maxi):
    
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

    
    neighbours = 0-grid[row][col]
    for nrow in range(minRow, maxRow+1):
        for ncol in range(minCol, maxCol+1):
            neighbours += grid[nrow][ncol]
    if grid[row][col] == 1 and neighbours <mini:
        return 0
    
    elif grid[row][col] == 1 and (mini <= neighbours <=maxi):
        return 1
    
    elif grid[row][col] == 1 and neighbours > maxi:
        return 0
    
    elif grid[row][col] == 0 and neighbours == maxi:
        return 1
    else:
        return 0


def randomGrid(gridSize):
    grid = []
    for row in range(0, gridSize):
        grid.append([])
        for col in range(0, gridSize):
            grid[row].append(randint(0, 1))
    return grid




def drawn_box(screen,px,py,size=50,color=color_muerto,width=0):
    rect = (px, py, size, size)
    pygame.draw.rect(screen, color, rect, width)

def drawn_Grid(screen,grid,px,py,size=50):
    pos_x=px
    pos_y=py
    i=0
    while i<len(grid):
        pos_y=py+size*i
        j=0
        while j<len(grid[0]):
            pos_x=px+size*j
            if grid[i][j]==1:
                if RANDON:
                    color=[randint(0,255),randint(0,255),randint(0,255)]
                else:
                    color=color_vivo
                drawn_box(screen,pos_x,pos_y,size,color,1)
            else:
                drawn_box(screen,pos_x,pos_y,size,color_muerto)
            j+=1
        i+=1

def main():
    pygame.init()

    top_left = 0
    top_righ = 0
    slip=0
    mini=2#2
    maxi=3#3
    size=10
    gridSize=100
    currentgrid=randomGrid(gridSize)

    nextgrid = []
    for row in range(gridSize):
        nextgrid.append([])
        for col in range(gridSize):
            nextgrid[row].append(0)


    
    
    screen = pygame.display.set_mode((gridSize*size, gridSize*size))
    pygame.display.set_caption("Juego de la vida")
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill([0,0,0])
        drawn_Grid(screen,currentgrid,top_left,top_righ,size)
        pygame.display.flip()
        if slip:
            time.sleep(0.1)

    
        for row in range(gridSize):
            for col in range(gridSize):
                nextgrid[row][col] = checkCell(row, col, currentgrid, gridSize,mini,maxi)
        tmpgrid = currentgrid
        currentgrid = nextgrid
        nextgrid = tmpgrid 


if __name__ == "__main__":
    main()

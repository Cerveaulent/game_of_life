from time import sleep as wait
from subprocess import run
from cell import Cell
from Rules import rule, update_all
import os

def print_grid(grid):
    print("")
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            print(grid[x][y], end=' ')
        print("")


def main():
    grid = [[Cell(x, y) for x in range(50)] for y in range(50)]
    grid[20][20].state = 1
    grid[20][21].state = 1
    grid[20][23].state = 1
    grid[21][22].state = 1
    grid[19][24].state = 1
    grid[19][19].state = 1
    grid[18][19].state = 1
    
    print_grid(grid)
    step = 0
    while step < 25:
        rule(grid)
        update_all(grid)
        os.system("clear")
        print_grid(grid)

        step += 1
        wait(1)


if __name__ == '__main__':
    main()

from time import sleep as wait
from subprocess import run

from cell import Cell
from Rules import rule, update_all


def print_grid(grid):
    print("")
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            print(grid[x][y], end=' ')
        print("")


def main():
    grid = [[Cell(x, y) for x in range(5)] for y in range(5)]
    grid[2][2].state = 1
    grid[3][2].state = 1
    grid[3][3].state = 1
    print_grid(grid)
    step = 0
    while step < 100:
        rule(grid)
        update_all(grid)
        print_grid(grid)
        step += 1
        wait(0.5)


if __name__ == '__main__':
    main()

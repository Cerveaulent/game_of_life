from cell import Cell


def check_neighb(x, y, grid):
	alive = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			if i == 0 and j == 0:
				continue
			elif (x + i < 0) or (len(grid) <= (x + i)):
				continue
			elif (y + j < 0) or (len(grid[0]) <= (y + j)):
				continue
			elif grid[x + i][y + j].state == 1:
				alive += 1
	if alive == 3:
		grid[x][y].next_state = 1
	elif alive == 2:
		grid[x][y].next_state = grid[x][y].state
	else:
		grid[x][y].next_state = 0


def rule(grid):
	for x in range(len(grid)):
		for y in range(len(grid[0])):
			check_neighb(x, y, grid)


def update_all(grid):
	for x in range(len(grid)):
		for y in range(len(grid[0])):
			grid[x][y].update()

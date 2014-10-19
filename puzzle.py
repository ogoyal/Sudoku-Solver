def sudoku():
	grid = [[0,0,0, 2,6,0, 7,0,1], [6,8,0, 0,7,0, 0,9,0], [1,9,0, 0,0,4, 5,0,0],
	        [8,2,0, 1,0,0, 0,4,0], [0,0,4, 6,0,2, 9,0,0], [0,5,0, 0,0,3, 0,2,8],
	        [0,0,9, 3,0,0, 0,7,4], [0,4,0, 0,5,0, 0,3,6], [7,0,3, 0,1,8, 0,0,0]]
	return grid

def UsedInRow(grid, row, num):
	for col in range(9):
		if(grid[row][col] == num):
			return True
	return False

def UsedInCol(grid, col, num):
	for row in range(9):
		if(grid[row][col] == num):
			return True
	return False

def UsedInBox(grid, boxStartRow, boxStartCol, num):
	for row in range(3):
		for col in range(3):
			if(grid[row+boxStartRow][col+boxStartCol] == num):
				return True
	return False


def isSafe(row, col, grid, num):
	return ((UsedInRow(grid,row,num) == False) and (UsedInCol(grid,col,num) == False) and (UsedInBox(grid, row - row%3, col - col%3, num) == False))

def FindUnassignedLocation(grid, row, col):
	if(grid[row][col] == 0):
		return True
	else:
		return False

def FullSudoku(grid):
	for row in range(9):
		for col in range(9):
			if(grid[row][col] == 0):
				return False
	return True

def solveSudoku(grid):
	
	if(FullSudoku(grid) == True):
		return True

	for i in range(9):
		for j in range(9):
			if(FindUnassignedLocation(grid, i, j) == True):
				row = i
				col = j

	for i in range(1,10):
		#print("num: ", i)
		if(isSafe(row, col, grid, i) == True):
			print("guess: ", i)
			grid[row][col] = i

			if(solveSudoku(grid) == True):
				return True

			grid[row][col] = 0 #unassigned

	return False

def printGrid(grid):
	for i in range(9):
		string = ""
		for j in range(9):
			string = string + str(grid[i][j]) + " "
		print(string)

def main():
	grid = sudoku()
	printGrid(grid)
	if(solveSudoku(grid) == True):
		printGrid(grid)
	else:
		print("no solution exists")

main()
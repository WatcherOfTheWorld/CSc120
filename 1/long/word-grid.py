#=================================================================================================
#   Assignment: 1 Long assignment 2
#       Author: Feiran Yang 
#
#       Course:  CSc 120
#   Instructor:  Saumya Debray
#
#  Description:  This program will read two user input as grid size and random number seed. the 
#				 program will then create an N * N lower-case letters grid randomly with the 
#				 random number seed and print the grid out.
#=================================================================================================
import random

def main():
	size = init()
	grid = make_grid(size)
	print_grid(grid)

#=================================================================================================
# Function Name:    init()
#       Purpose:    read the user input as size and seed_gen, use seed_gen as seed to initialize 
#					random number. return size in the end.
#    Parameters:    N/A
#       Returns:    size
#=================================================================================================
def init():
	size = input()
	seed_gen = input()
	random_number = random.seed(seed_gen)

	return size

#=================================================================================================
# Function Name:    make_grid(size)
#       Purpose:    take size from main as parameter. creat an size * size list of list with
#					generated random letter. return that list of list in the end.
#    Parameters:    size
#       Returns:    gird
#=================================================================================================
def make_grid(size):
	size = int(size)
	grid = [0] * size
	for i in range(0,size):
		grid[i] = [0] * size
		for j in range(0, size):
			# random number using seed and transfer number ASCII characters
			new_chr = random.randint(97,122)  
			grid[i][j] = chr(new_chr)
	return grid

#=================================================================================================
# Function Name:    init()
#       Purpose:    take grid as parameter. print that grid out so it looks like a grid. 
#    Parameters:    grid
#       Returns:    N/A
#=================================================================================================
def print_grid(grid):
	for i in range(0, len(grid)):
		for j in range(0, len(grid)-1):
			print(grid[i][j]+',',end ='')
		print(grid[i][j+1])


main()
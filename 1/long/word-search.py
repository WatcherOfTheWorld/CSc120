#=================================================================================================
#   Assignment: 1 Long assignment 1
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  This program will read user input by order, a word of list file and a grid file
#				 It will then transfer grid file in to a grid list. search this grid for and legal
#				 case-insensitive words that exist in list of words file. print those word with 
#				 a specific print format
#=================================================================================================
def main():
    list_word, grid = user_input()

    result = search_words(list_word, grid)
    display(result, 'hori')

    rotated_grid = rotate_grid(grid)
    result = search_words(list_word, rotated_grid)
    display(result, 'vert')

    diamond_grid = diagonal_grid(grid)
    result = search_words(list_word, diamond_grid)
    display(result, 'diagonal_tl_br')

    reflected_grid = reflect_grid(grid)
    diamond_reflected_grid = diagonal_grid(reflected_grid)
    result = search_words(list_word, diamond_reflected_grid)
    display(result, 'diagonal_tr_bl')
 

#=================================================================================================
# Function Name:    user_input()
#       Purpose:    take two user input as list of words and grid of letter. Convert them to a 
#					list
#    Parameters:    N/A
#       Returns:    return two converted list(list_word, grid)
#=================================================================================================
def user_input():
	list_word = input()
	grid = input()
	# raed grid file, put in into a list of list
	grid = open(grid).readlines()
	for i in range(0,len(grid)):
		grid[i] = grid[i].strip('\n').split()
	list_word = open(list_word).readlines()
	for i in range(0,len(list_word)):
		list_word[i] = list_word[i].strip('\n')

	return list_word, grid

#=================================================================================================
# Function Name:    search_words(list_word, grid)
#       Purpose:    take a grid of letter, assmble them to a word then call a function to check if
#					it is legal. collect those legal words into a list.
#    Parameters:    list_word, grid
#       Returns:    (hori_l_r, hori_r_l)
#=================================================================================================
def search_words(list_word, grid):
	hori_l_r = []
	hori_r_l = []
	for i in range(0,len(grid)):
		# use to make a list left side right.
		reversed_list = [0] * len(grid)
		for d in range(0,len(grid[i])):
			reversed_list[d] = grid[i][-d-1]
		# find the words in list and reversed list
		for j in range(0, len(grid[i])-1):
			for c in range(0, len(grid[i])-j-2):
				temp_list = grid[i][c:c+j+3]
				key = make_words(temp_list)
				if occurs_in(key, list_word):
					hori_l_r.append(key)

				temp_list = reversed_list[c:c+j+3]
				key = make_words(temp_list)
				if occurs_in(key, list_word):
					hori_r_l.append(key)

	return hori_l_r, hori_r_l
	print(hori_l_r)
	print(hori_r_l)

#=================================================================================================
# Function Name:    rotate_grid(grid)
#       Purpose:    take a grid of letter as parameter, rotate that grid to a new list of list
#					return that new gird.
#    Parameters:    grid
#       Returns:    return one ratated grid.
#=================================================================================================
def rotate_grid(grid):
	new_grid = [0] * len(grid)
	for i in range(0, len(grid)):
		temp_list = []
		for j in range(0, len(grid)):
			temp_list.append(grid[j][i])
		new_grid[i] = temp_list
	return new_grid

#=================================================================================================
# Function Name:    diagonal_grid(grid)
#       Purpose:    take a grid of letter as parameter, rotate it 45 degree(to make it looks like
#					diaganal). collect those letter into a new list of diagonal grid. then remove
#					any element that have less that 3 letter. return the final new grid to mian
#    Parameters:    grid
#       Returns:    new_grid
#=================================================================================================
def diagonal_grid(grid):
	new_grid = []
	for i in range(0,len(grid)):
		list_hori = []
		list_vert = []
		for j in range(i, len(grid)):
			list_hori.append(grid[j-i][j])
			list_vert.append(grid[j][j-i])
		new_grid.append(list_hori)
		new_grid.append(list_vert)
	# delete the repeat list
	del new_grid[0]
	# delete the list in list of list that has less then 3 elements
	for i in range(0, 4):
		del new_grid[-1]
	return new_grid

#=================================================================================================
# Function Name:    reflect_grid(grid)
#       Purpose:    reflect a grid up-side-down, then return that new grid
#    Parameters:    grid
#       Returns:    new_grid
#=================================================================================================
def reflect_grid(grid):
	new_grid = [0] * len(grid)
	for i in range(0, len(grid)):
		new_grid[i] = grid[-i-1]
	return new_grid

#=================================================================================================
# Function Name:    occurs_in(key, list_word)
#       Purpose:    take a key word, check if it is in list_word. if yes, return Ture
#    Parameters:    key, list_word
#       Returns:    return two converted list(list_word, grid)
#=================================================================================================
def occurs_in(key, list_word):
	for i in range(0, len(list_word)):
		# if it hapeend in list of word, return True
		if key == list_word[i].lower():
			return True

#=================================================================================================
# Function Name:    make_words(temp_list)
#       Purpose:    take a parameter call temp_list contain group of letter, assmble it to a str.
#					return that str
#    Parameters:    temp_list
#       Returns:    key
#=================================================================================================
def make_words(temp_list):
	key = ''
	# assmble a new words
	for i in range(0, len(temp_list)):
		key += temp_list[i]
	return key

#=================================================================================================
# Function Name:    display(result, dir)
#       Purpose:    take two parameters as two list of collection of legal words and direction of 
#					list. translate direction to direction describe. call print result to print 
#					on console
#    Parameters:    result, dir
#       Returns:    N/A
#=================================================================================================
def display(result, dir):
	left_right, right_left = result
	# tranlate direction indicater into descripition of list
	if dir == 'hori':
		dir_describe_lr = '(horizontal, L-to-R)'
		dir_describe_rl = '(horizontal, R-to-L)'
	elif dir == 'vert':
		dir_describe_lr = '(vertical, top-to-bottom)'
		dir_describe_rl = '(vertical, bottom-to-top)'
	elif dir == 'diagonal_tl_br':
		dir_describe_lr = '(diagonal, top-left to bottom-right)'
		dir_describe_rl = '(diagonal, bottom-right to top-left)'
	elif dir == 'diagonal_tr_bl':
		dir_describe_lr = '(diagonal, bottom-left to top-right)'
		dir_describe_rl = '(diagonal, top-right to bottom-left)'

	print_result(left_right, dir_describe_lr)
	print_result(right_left, dir_describe_rl)

#=================================================================================================
# Function Name:    print_result(list, dir_describe)
#       Purpose:    take two parameters as collection of legal words and direction describe. print
#					them if the length of legal words collection is not 0
#    Parameters:    list, dir_describe
#       Returns:    N/A
#=================================================================================================
def print_result(list, dir_describe):	
	# make sure the length of list is large than 0
	if len(list) != 0:
		for i in range(0, len(list)-1):
			print(list[i] + ',', end='')
		print(list[-1] + ' ' + dir_describe)

main()

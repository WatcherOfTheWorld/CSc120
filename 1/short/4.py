def column2list(grid, n):
	list = []
	for i in range(0, len(grid)):
		list.append(grid[i][n])

	print(list)
	return list


column2list([ [ 'aa', 'bb', 'cc', 'dd' ],[ 'ee', 'ff', 'gg', 'hh', 'ii', 'jj' ],[ 'kk', 'll', 'mm', 'nn' ] ],3)
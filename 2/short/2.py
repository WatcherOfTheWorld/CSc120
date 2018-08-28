list2d = [[ 'aa', 'bb', 'cc', 'dd' ],[ 'ee', 'ff', 'gg', 'hh', 'ii', 'jj' ],[ 'kk', 'll', 'mm', 'nn' ] ]
def list2dict(list2d):
	dict = {}
	for i in range(0,len(list2d)):
		dict[list2d[i][0]] = list2d[i][1:]
	return dict
list2dict(list2d)
def invert_dict(origdict):
	item = list(origdict.items())
	key = []
	val = []
	for i in range(0,len(item)):
		val.append(item[i][0])
		key.append(item[i][1])
		
	dict = {}
	for i in range(0,len(key)):
		dict[key[i]] = val[i]
	return dict
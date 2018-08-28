somedict = { 'a' : 12, 'b' : 93, 'c' : 47}
def shuffle_dict(somedict):
	item = list(somedict.items())
	key = []
	val = []
	for i in range(0,len(item)):
		key.append(item[i][0])
		val.append(item[i][1])
	key.sort()
	val.sort()

	dict = {}
	for i in range(0,len(key)):
		dict[key[i]] = val[i]
	return dict
shuffle_dict(somedict)
DD = { 'aaa' : { 'bbb' : 'string1', 'ccc' : 'string2', 'ddd' : 'string3' },
	   'bbb' : { 'ccc' : 'string4', 'ddd' : 'string5', 'eee' : 'string6', 'fff' : 'string7' },
	   'ccc' : { 'aaa' : 'string8', 'bbb' : 'string9' }}
def update_dict2(dict2, key1, key2, value):
	key_1 = dict2.keys()
	if not key1 in key_1:
		dict0[key2] = value
		dict2[key1] = dict0

	dict2[key1][key2] = value
	return dict2

update_dict2(DD,'ggg','aaa','string17')
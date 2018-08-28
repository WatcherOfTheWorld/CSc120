def ngram(arglist, startpos, length):
	if startpos + length > len(arglist):
		return []
	return arglist[startpos:startpos + length]
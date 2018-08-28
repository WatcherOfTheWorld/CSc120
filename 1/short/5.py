def grid_is_square(arglist):
	hori = len(arglist)
	for i in range(0,hori):
		if len(arglist[i]) != hori:
			print ("False")
	print ("True")

grid_is_square([[0,1,2,3,4],[3,4,5,6,7],[4,5,6,7,8]])
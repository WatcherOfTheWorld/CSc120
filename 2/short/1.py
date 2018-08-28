def sum_csv_string(csv_string):
	list = csv_string.split(",")
	sum = 0
	for i in range(0,len(list)):
		sum += int(list[i])
	print(sum)
sum_csv_string("11,22,-33")

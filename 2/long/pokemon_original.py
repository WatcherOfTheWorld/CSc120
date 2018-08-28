#=================================================================================================
#   Assignment: Long assignment 2
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  This program will import a pokemon infomation CVS file at the begining. and read 
# 				 those pokemon date into a dictionary of dictionary. pre-compute the average value
#				 of each type of pokemon. apend average value list to poke_type dictionary.
#				 after computing average value, take a query from user and print the corresponding
#				 data in terminal.
#=================================================================================================
def main():
	poke_type = read()
	poke_type = pre_computing(poke_type)
	
	# initialize the while loop and make the order nubmer become -1
	order_nubmer = -1
	while order_nubmer >= -1:
		order = input()
		order_nubmer = order_list(order)
		# if order_number not -1 or -2(if user input a value input and did not input a empty str)
		# print the pokemon data in terminal.
		if order_nubmer >= 0 :
			dispaly(poke_type, order_nubmer)

#=================================================================================================
# Function Name:    read()
#       Purpose:    import a Pokemon.csv file. read data in Pokemon.csv file into a dictionary of
#				    dictionary. and return that dictionary of dictionary to main.
#    Parameters:    N/A
#       Returns:    poke_type
#=================================================================================================
def read():
	poke_info = input()
	pokemon = open(poke_info).readlines()
	# remove unuseful info from list
	for i in range(1,len(pokemon)):
		pokemon[i] = pokemon[i].strip("\n")
		pokemon[i] = pokemon[i].split(',')
	del pokemon[0]

	# creat a dict use pokemon's name as key and maping to other datas
	poke_dict = {}
	for i in range(0, len(pokemon)):
		poke_dict[pokemon[i][1]] = pokemon[i][1:]
	
	# creat a upper level dict use pokemon type as key and maping to poke_dict
	poke_type = {}
	for i in poke_dict:
		if poke_dict[i][1] in poke_type:
			poke_type[poke_dict[i][1]][i] = poke_dict[i][3:-1]
		else:
			poke_type[poke_dict[i][1]] = {i:poke_dict[i][3:-1]}

	return poke_type

#=================================================================================================
# Function Name:    pre-computing(poke_type)
#       Purpose:    take poke_type as a parameter. loop in side the dict of dict and calculate the
#					a verage value for each of pokemon. append that average value list into the 
#					dict and return the updated dict
#    Parameters:    poke_type
#       Returns:    poke_type
#=================================================================================================
def pre_computing(poke_type):
	# calculate the average value for each attributes and for each type
	for i in poke_type:
		keys = list(poke_type[i].keys())
		count = [0] * len(poke_type[i][keys[0]])
		for j in poke_type[i]:
			for k in range(0, len(poke_type[i][j])):
				count[k] += int(poke_type[i][j][k])

		for x in range(0,len(poke_type[i][keys[0]])):
			count[x] = count[x]/len(keys)

		# apped attributes list to the dict of dict
		poke_type[i][0]=count

	return poke_type

#=================================================================================================
# Function Name:    order_list(order)
#       Purpose:    take user's input as a parameter(query). return that order as index in dict of
#					dict.
#    Parameters:    order
#       Returns:    index number
#=================================================================================================
def order_list(order):
	order.lower()
	if order == "total":
		return 0
	elif order == "hp":
		return 1
	elif order == "attack":
		return 2
	elif order == "defense":
		return 3
	elif order == "specialattack":
		return 4
	elif order == "specialdefense":
		return 5
	elif order == "speed":
		return 6
	# if user typed nothing, return -2 to end the program.
	elif order == "":
		return -2
	# if user typed somethink else, return -1 to ignro that input.
	else:
		return -1

#=================================================================================================
# Function Name:    display(poke_type, order)
#       Purpose:    take poke_type and order(index) as parameters. find the max average value for 
#					that index. and print the max average using format()
#    Parameters:    poke_type, prder
#       Returns:    null
#=================================================================================================
def dispaly(poke_type, order):
	# compare and save the max value and type has max value
	max = [0,0]
	for i in poke_type:
		value = poke_type[i][0][order]
		if value > max[0]:
			max = [0,0]
			max[0] = value
			max[1] = i

		# if two types of pokemon have same max average 
		elif value == max[0]:
			max.append(value)
			max.append(i)

	# print analysised data with format() method
	for i in range(0, len(max), 2):
		pokemon_type, max_average = max[i + 1], max[i]
		print("{}: {}".format(pokemon_type, max_average)) 

main()
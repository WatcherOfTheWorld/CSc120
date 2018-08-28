#=================================================================================================
#   Assignment: Long assignment 4 Biodiversity
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  This program will input and read a 2 CSV file in to two list. pack data from both
#				 list into a dictionary. then compute the average fauna or flora pre acre.
#=================================================================================================
def main():
	parks = read_in()
	species = read_in()
	park_db(parks, species)


#=================================================================================================
# Function Name:    read_in()
#       Purpose:    will ask user to input a file name first. then read in that file to a list.
#					close the file and return the list in the end.
#    Parameters:    N/A
#       Returns:    data
#=================================================================================================
def read_in():
	# get user input and open file
	file_name = input()
	open_file = open(file_name)
	data = open_file.readlines()
	# remove the first line that start with '#'
	if data[0][0] == '#':
		del data[0]
	# split every elements by ','
	for i in range(0, len(data)):
		assert type(data[i]) == str
		data[i] = data[i].split(',')

	open_file.close()
	return data

#=================================================================================================
# Function Name:    park_db
#       Purpose:    take 2 lists as parameters from main. creat a new dictionary and add every 
#				    elements in parks as key mapping to acre of park and numbers of flora and 
#					fauna. call prit_out function in the and to pre-print data.
#    Parameters:    parks, species
#       Returns:    N/A
#=================================================================================================
def park_db(parks, species):
	# creat a dictionary with parks name as key
	db = {}
	for i in range(0, len(parks)):
		assert len(db) <= i 
		db[parks[i][0]] = (parks[i][2], [0], [0])

	# count the total numbers of flora and fauna
	for i in range(0, len(species)):
		assert type(species) == list
		if species[i][0] in db:
			if species[i][1] == 'Algae' or species[i][1] == 'Fungi' or \
			   species[i][1] == 'Nonvascular Plant' or species[i][1] == 'Vascular Plant' :
				cate = 1

			elif species[i][1] == 'Amphibian' or species[i][1] == 'Bird' or \
			     species[i][1] == 'Crab/Lobster/Shrimp' or species[i][1] == 'Fish' or \
			     species[i][1] == 'Insect' or species[i][1] == 'Invertebrate' or \
			     species[i][1] == 'Mammal' or species[i][1] == 'Reptile' or \
			     species[i][1] == 'Slug/Snail' or species[i][1] == 'Spider/Scorpion' :
				cate = 2
			# if the species is not both flora or fauna, do not add anything.
			else:
				cate = 0

			if not cate == 0:
				db[species[i][0]][cate][0] += 1

	# run a loop to call print_out() to print data
	for i in db:
		assert type(db[i]) == tuple
		print_out(i, db[i][0], db[i][1][0], db[i][2][0])

#=================================================================================================
# Function Name:    print_out()
#       Purpose:    take park_name, acre, flora, fauna as perameters, cheak if the data is 
#					avaliable. if not, print not avaliable, otherwise print all data out.
#    Parameters:    park_name, acre, flora, fauna
#       Returns:    N/A
#=================================================================================================
def print_out(park_name, acre, flora, fauna):
	assert type(flora) == int and type(fauna) == int
	# cheak if both flora and fauna is 0
	if flora == 0 and fauna == 0:
		print("{} -- no data available".format(park_name))
	# if not, cumpute all the data and print them out.
	else:
		if flora == 0:
			fauna_per_acre = fauna / int(acre)
			flora_per_acre = 0
		if fauna == 0:
			flora_per_acre = flora / int(acre)
			fauna_per_acre = 0
		else:	
			flora_per_acre = flora / int(acre)
			fauna_per_acre = fauna / int(acre)
		print("{} -- flora: {:f} per acre; fauna: {:f} per acre".format(park_name, flora_per_acre, fauna_per_acre))

main()
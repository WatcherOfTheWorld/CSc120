#=================================================================================================
#   Assignment: Long assignment 4 Abundance
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  This program will input and read a 2 CSV file in to two list. pack data from both
#				 list into a dictionary. then compute the average fauna or flora pre acre.
#=================================================================================================
def main():
	sinfo = read_in()
	count_species(sinfo)

#=================================================================================================
# Function Name:    read_in()
#       Purpose:    will ask user to input a file name first. then read in that file to a list.
#					close the file and return the list in the end.
#    Parameters:    N/A
#       Returns:    sinfo
#=================================================================================================
def read_in():
	# get user input and open file
	sinfo_name = input()
	sinfo_file = open(sinfo_name)
	sinfo = sinfo_file.readlines()
	# remove the first line that start with '#'
	if sinfo[0][0] == '#':
		del sinfo[0][0]
	# split every elements by ','
	for i in range(0, len(sinfo)):
		assert type(sinfo[i]) == str
		sinfo[i] = sinfo[i].split(',')
	sinfo_file.close()

	return sinfo

#=================================================================================================
# Function Name:    count_species()
#       Purpose:    creat a dictionary. maping parks name(lower) to species name(lower). then 
#					covert every elements in that dictionart to set. call print_data in the end
#					to print data
#    Parameters:    sinfo
#       Returns:    N/A
#=================================================================================================
def count_species(sinfo):
	db = {}
	for i in range(0, len(sinfo)):
		assert type(sinfo) == list
		if not sinfo[i][2].lower() in db:
			db[sinfo[i][2].lower()] = []
		db[sinfo[i][2].lower()] += [sinfo[i][0].lower()]

	# covert list in dict to set to avoid repeat elements.
	for i in db:
		assert type(db[i]) == list
		db[i] = set(db[i])

	print_data(db)

#=================================================================================================
# Function Name:    print_data()
#       Purpose:    take db as a parameter, init a list for finding max nubmer. after finding the
#					max number, print the max nubmer out 
#    Parameters:    N/A
#       Returns:    data
#=================================================================================================
def print_data(db):
	count = [0, 0]
	for i in db:
		assert len(count) % 2 == 0
		# if db[i] is big the max number stored in count, replace that max nubmer and species name
		if len(db[i]) > count[1]:
			count = [i, len(db[i])]
		# if there the same, append the max number and species name.
		elif len(db[i]) == count[1]:
			count.append(i)
			count.append(len(db[i]))

	# go into a loop, too print all data out.
	for i in range(0, len(count), 2):
		assert type(count[1]) == int
		species_name = count[i]
		number_of_parks = count[i + 1]
		print("{} -- {:d} parks".format(species_name, number_of_parks))

main()
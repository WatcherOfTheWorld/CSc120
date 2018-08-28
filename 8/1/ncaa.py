#=================================================================================================
#   Assignment: Long assignment 8 nacc.py
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  This program read in a user input as file name. procces file into a dict.
#				 then ask user for round, and probability.
#				 find the team meet the proability in that round and print out team name and prob.
#=================================================================================================
from operator import*

def main():
	team_dict = input_file()
	start = 0 
	while start == 0:
		rounds, prob, do_continue = input_data()
		# if there is error happen when transfer data to int or float
		if do_continue:
			# continue the loop
			continue
		find(team_dict, rounds, prob)

#=================================================================================================
# Function Name:    input_file()
#       Purpose:    ask user for a file input, open the file and process data in to a dict.
#					if can not be open, quit the program
#    Parameters:    N/A
#       Returns:    team_dict
#=================================================================================================
def input_file():
	file_name = input("Data file: ")
	# try to open
	try:
		lines = open(file_name).readlines()
	# if falled, exit
	except IOError:
		print("{} {}".format("ERROR: Could not open file", file_name))
		exit(1)
	# remove first line start with #
	if lines[0][0] == '#':
		del lines[0]

	team_dict = {}
	for i in range(0, len(lines)):
		# split lines
		lines[i] = lines[i].split(',')
		# covers data to float number and add to dict
		data = lines[i][3:9]
		for j in range(0, len(lines[i][3:9])):
			try:
				data[j] = float(data[j])
			# if covert error, set data to not legit value and print an error
			except ValueError:
				data[j] = -99.0
				print('ERROR: illegal query value(s)') 
		team_dict[lines[i][12]] = data
	return team_dict

#=================================================================================================
# Function Name:    input_data()
#       Purpose:    reading user input, covert to int or float, if falled, pass loop outside this 
#					function, or not in range, exit
#    Parameters:    N/A
#       Returns:    rounds, probability, do_continue
#=================================================================================================
def input_data():
	do_continue = False 
	rounds = input('Rounds: ')
	# if input nothing,exit
	if rounds == '':
		exit(0)
	# try covert to int and float
	try:
		probability = input('Probability: ')
		rounds = int(rounds) - 1
		probability = float(probability)
	except ValueError:
		print('ERROR: illegal query value(s)') 
		do_continue = True

	if not do_continue:
		# assert make sure range is right	
		assert 0 <= rounds <= 6
		assert 0 <= probability <= 1
	return rounds, probability, do_continue

#=================================================================================================
# Function Name:    find()
#       Purpose:    take team_dict, rounds, prob from main. find team meets requirment and print 
#					team name and data out
#    Parameters:    team_dict, rounds, prob
#       Returns:    N/A
#=================================================================================================
def find(team_dict, rounds, prob):
	# get a list contain team name and data that data of rounds is larger than prob
	plist= [(team,team_dict[team][rounds]) for team in team_dict if team_dict[team][rounds]>=prob]
	# sort the list
	plist = sorted(plist, key=itemgetter(1), reverse=True)
	# print them out
	for i in range(0, len(plist)):
		team, probability = plist[i]
		print("{} : {:f}".format(team, probability))


main()
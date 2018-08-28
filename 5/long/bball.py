#=================================================================================================
#   Assignment: Long assignment 5 bball.py
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  This file include 3 class and a main program. this program wlll read a file in 
#				 and call class Team to process each line to count win ratio for each team.
#				 after counting win ratio, call class Conference to compute win ratio for each 
#				 conf. and find conference has the best win ratio and print the data out by call
#				 class ConferenceSet
#=================================================================================================

#=================================================================================================
# 	 Class Name:    Team
#       Purpose:    represents name, conferencem win&lost about a team
#=================================================================================================
class Team:
	#=================================================================================================
	# 	Method Name:    __init__()
	#       Purpose:    init the class process a line taking from main program.
	#    Parameters:    line
	#       Returns:    N/A
	#=================================================================================================
	def __init__(self, line):
		# split a line into diffrent piece
		line = line.split('(')
		for i in range(0, len(line)):
			assert type(line) == list
			line[i] = line[i].split(')')
		line[-1][-1] = line[-1][-1].split('\t')

		# make a empty list to find the empty piece of str
		empty = []
		for i in range(0, len(line[-1][-1])):
			assert type(line[-1][-1]) == list
			if line[-1][-1][i] == '':
				empty.append(i)
		# del empty str
		for i in range(len(empty)-1, 0 -1, -1):
			assert line[-1][-1][empty[i]] == ''
			del line[-1][-1][empty[i]]

		self.__name = line[0][0]
		self.__conf = line[-1][0]
		# compute the win ratio
		self.__win_ratio = int(line[-1][-1][-2]) / (int(line[-1][-1][-2]) + int(line[-1][-1][-1]))

	# return the name of the team
	def name(self):
		return self.__name

	# return the conf name of the team
	def conf(self):
		return self.__conf

	# return the win ratio of the team
	def win_ratio(self):
		return self.__win_ratio

	# str method use to print
	def __str__(self):
		return "{} : {}".format(self.__name, str(self.__win_ratio)) 

#=================================================================================================
# 	 Class Name:    Conference
#       Purpose:    represents team set, name and avg win rantio of a conf
#=================================================================================================
class Conference:
	# init the class
	def __init__(self, conf):
		self.__conf_name = conf
		self.__conf = []
		self.__avg = 0.0

	# return ture is team is in this conf
	def __contains__(self, team):
		return team in self.__conf

	# return the name of this conf
	def name(self):
		return self.__conf_name

	# add a team to this conf
	def add(self, team):
		assert type(self.__conf) == list
		self.__conf.append(team)

	#=================================================================================================
	# 	Method Name:    win_ratio_avg()
	#       Purpose:    compute the avg win ratio of this conf
	#    Parameters:    N/A
	#       Returns:    self.__avg
	#=================================================================================================
	def win_ratio_avg(self):
		count = 0
		# add win ratio of every team in that conf to count
		for i in range(0, len(self.__conf)):
			assert type(self.__conf[i].win_ratio()) == float
			count += self.__conf[i].win_ratio()

		# didided by total team
		self.__avg = count / len(self.__conf)
		return self.__avg 

	# str method use to print
	def __str__(self):
		return "{} : {}".format(self.__conf_name, str(self.__avg)) 

#=================================================================================================
# 	 Class Name:    Team
#       Purpose:    represents set of conferencem and a conf has the best win%lost rate 
#=================================================================================================
class ConferenceSet:
	# make a empty conf set
	def __init__(self):
		self.__conf_set = []

	# add team each conf set
	def add(self, team):
		self.__conf_set.append(team)

	#=================================================================================================
	# 	Method Name:    best()
	#       Purpose:    find the best win ratio.
	#    Parameters:    N/A
	#       Returns:    largest_conf
	#=================================================================================================	
	def best(self):
		# get all conf in a set
		conf_set = list(set(self.__conf_set))
		large = 0
		largest_conf = []
		# loop trough the conf set
		for i in range(0, len(conf_set)):
			assert type(conf_set) == list
			# if a conf's avg is large the pre lragest one 
			if large < conf_set[i].win_ratio_avg():
				# rewirte large as it's number
				large = conf_set[i].win_ratio_avg()
				# rewrite largest conf as it inside of a list
				largest_conf = [conf_set[i]]
			# if lrage == to this conf' avg
			elif large == conf_set[i].win_ratio_avg():
				# append this conf to largest conf list
				largest_conf.append(conf_set[i])

		return largest_conf


def main():
	database = input_file()
	compare(database)

#=================================================================================================
# Function Name:    input_file()
#       Purpose:    aks user for a input file name, open the file del all the line start with '#'
#					and strip all '\n' at the end of every line. call Team to get every win%lost
#					rate and add them into a dict.
#    Parameters:    N/A
#       Returns:    database
#=================================================================================================
def input_file():
	file_name = input()
	data = open(file_name).readlines()
	# del every line start with '#'
	for i in range(0, len(data)):
		assert type(data) == list
		if data[0][0] == '#':
			del data[0]
	# del every '\n' at every end of the line
	for i in range(0, len(data)):
		assert data[i][0] != '#'
		data[i] = data[i].strip('\n')

	# make a new data base
	database = {}
	# map team name and win ratio to each conf
	for i in range(0, len(data)):
		assert type(data[i]) == str
		a_team = Team(data[i])
		if a_team.conf() in database:
			database[a_team.conf()].append([a_team, a_team.win_ratio()])
		else: 
			database[a_team.conf()] = [[a_team, a_team.win_ratio()]]
	return database

#=================================================================================================
# Function Name:    compara()
#       Purpose:    call conferenceSet to init it. call conference to init class conference. add
#					each team to diffrent conf and get the avf win ratio. find the max ratio by
#					calling best() in conf_set
#    Parameters:    database
#       Returns:    N/A
#=================================================================================================
def compare(database):
	# init ConferenceSet
	conf_set = ConferenceSet()
	# add every team to conference
	for conf in database:
		class_conf = Conference(conf)
		for i in range(0, len(database[conf])):
			assert type(database) == dict
			class_conf.add(database[conf][i][0])
		# get the avg win ratio for each conf
		avg = class_conf.win_ratio_avg()
		# add each team to conf set
		conf_set.add(class_conf)

	#find the best ratio by calling conf_set.best()
	best = conf_set.best()
	for i in range(0, len(best)):
		# print data
		print(best[i])

main()




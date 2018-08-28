#=================================================================================================
#   Assignment: Long assignment 8 co2.py
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  This program read in a file and process data in file to a list, check if data has
#				 error. then read 4 user input for field, range and if gragh.
#				 if user what gragh, show a gragh with data meet the field and range requirement
#				 otherwise, print those data out.
#=================================================================================================
from scatterplot import *

FILE_NAME = 'co2_levels.csv' # File name

def main():
	data_dict = process_file()
	field, start, stop, graph = user_input()
	
	display_data(data_dict, field, start, stop, graph)

#=================================================================================================
# Function Name:    process_file()
#       Purpose:    reading the file, covert to a list. process list to a list of list and covert
#					data to int or float point number. if there is error in data, print a error
#					message and continue. if cant open file, print can not open file and exit.
#    Parameters:    N/A
#       Returns:    data_dict
#=================================================================================================
def process_file():
	# try open file
	try:
		lines = open(FILE_NAME).readlines()
	# if file can not be open, exit
	except IOError:
		print("{} {}".format('Error: File Not Found', FILE_NAME))
		exit(1)
	# remove first line with '#'
	if lines[0][0] == '#':
		del lines[0]
	data_dict = []
	# process lines
	for i in range(0, len(lines)):
		# remove usless data and process it to a list of list
		lines[i] = lines[i].strip('\n').split(',')
		data_value = lines[i][3:]
		data_sub_value = ''
		# set default error statment to false
		error = False
		# try to covert co2 reading to float point number
		for j in range(0, len(data_value)):
			try:
				data_value[j] = float(data_value[j])
			# if falled and value is not '', set that data to empty str and error statment to ture
			except ValueError:
				if data_value[j] != '':
					data_sub_value = data_value[j]
					data_value[j] = ''
					error = True
		# try to append data to data_dict and covert year and mounth to int
		try:
			data_dict.append([(int(lines[i][0]),int(lines[i][1])),data_value])
		# if falled, set error statment to ture
		except ValueError:
			error  = True

		# if error did occur, print error mess
		if error:
			print("ERROR: [line {:d}]: Bad value(s): {} {} {}".format(i+1, lines[i][0], lines[i][1], data_sub_value))

	return data_dict
		
#=================================================================================================
# Function Name:    user_input()
#       Purpose:    ask user for 4 input,and covert them to int. if falled return a error and exit
#    Parameters:    N/A
#       Returns:    field, start, stop, graph
#=================================================================================================
def user_input():
	# ask for input
	field = input("field [one of 3,4,5,6]: ")
	start = input("start year: ")
	stop = input("stop year: ")
	graph = input("graph? [y/n] ")
	# try to covert
	try:
		field = int(field)
		start = int(start)
		stop = int(stop)
	# if falled, print error and quit
	except ValueError:
		print("ERROR: illegal value for field")
		exit(1)

	# assert if field is in right range
	assert 3 <= field <= 6
	field -= 3

	return field, start, stop, graph

#=================================================================================================
# Function Name:    display_data(data_dict, field, start, stop, graph)
#       Purpose:    get data from main
#					if user ask or gragh, creat a list of tuple with index and data in side. then 
#					make a gragh.
#					other wise just print date and data to console
#    Parameters:    data_dict, field, start, stop, graph
#       Returns:    N/A
#=================================================================================================
def display_data(data_dict, field, start, stop, graph):
	# if user do want graph
	if graph == 'y':
		# set a index
		indx = range(len(data_dict))
		# creat a list of tuple with index and data inside
		data_list=[(i+1,data_dict[i][1][field]) for i in indx if start<=data_dict[i][0][0]<=stop and data_dict[i][1][field]!='']
		# call draw_scatterplot to graph
		draw_scatterplot(data_list, 'black', '#')

	# if user do not want graph
	else:
		# creat a list of date and data inside
		data_list=[(line[0][0],line[0][1],line[1][field]) for line in data_dict if start<=line[0][0]<=stop and line[1][field]!='']
		# print them out
		for i in range(0, len(data_list)):	
			year, month, data_value = data_list[i]
			print("{:d} {:d} -- {:f}".format( year, month, data_value ))


main()
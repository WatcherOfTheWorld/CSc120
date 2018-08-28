#=================================================================================================
#   Assignment: Long assignment 5 ngrams.py
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  This file include 2 class and a main program. this program wlll read a file and a
#				 n number to find how many times n-gram occurrs.
#=================================================================================================

#=================================================================================================
# 	 Class Name:    Input
#       Purpose:    read user's input and open a file. and process every words in that file.
#=================================================================================================
class Input:
	# aks user for a input, and open a file
	def __init__(self):
		name = input()
		self.__data = open(name).read()

	# split every line, make it all lower case, del every notation that is not inside of the words
	def wordlist(self):
		self.__data = self.__data.split()
		for i in range(len(self.__data) - 1, -1, -1):
			assert type(self.__data) == list
			self.__data[i] = self.__data[i].strip('~!@#$%^&*()-=_+[];,./:<>?|}{\\\'\"').lower()
			if self.__data[i] == '':
				# del empty str
				del self.__data[i]

		return self.__data

#=================================================================================================
# 	 Class Name:    Ngrams
#       Purpose:    ask user for a n input. and find the ngram occurrsed the most
#=================================================================================================
class Ngrams:
	# ask user for input and init a dict
	def __init__(self):
		self.__n = int(input())
		self.__dict = {}

	# update ngram
	def update(self, ngram):
		assert type(ngram) == int
		self.__dict[ngram] += 1

	# find how many times each ngram occurrsed 
	def process_wordlist(self, wordlist):
		n = self.__n
		# make a new list, append every ngrame tuple to that list 
		word_comb = []
		for i in range(0, len(wordlist) - n + 1):
			assert type(wordlist) == list
			word_comb.append(tuple(wordlist[i:i+n]))

		i = n
		# into a loop, computing how many time a ngrame happend.
		while not i >= len(word_comb):
			assert type(word_comb) == list
			for j in range(len(word_comb)-1, i - 1, -1):
				assert type(word_comb[i]) == type(word_comb[j])
				if word_comb[i] == word_comb[j]:
					if word_comb[j] in self.__dict:
						self.__dict[word_comb[i]] += 1
					else:
						self.__dict[word_comb[i]] = 1
					# del the element that has been count
					del word_comb[j]
		#add missing element into dic
		for j in range(0, len(word_comb)):
			assert type(word_comb[j]) == tuple
			if word_comb[j] in self.__dict:
				self.__dict[word_comb[j]] += 1
			else:
				self.__dict[word_comb[j]] = 1

	# print the max ngrams and the time it occurrsed.
	def print_max_ngrams(self):
		greatest = 0
		greatest_gram = []
		# find the max ngrams
		for gram in self.__dict:
			assert type(self.__dict) == dict
			if self.__dict[gram] > greatest:
				greatest = self.__dict[gram]
				greatest_gram = [gram]
			elif self.__dict[gram] == greatest:
				greatest_gram.append(gram)

		# print the max ngrams
		for i in range(0, len(greatest_gram)):
			# male ngrams tuple to a ngrams str
			ngram_string = greatest_gram[i][0]
			for j in range(1, len(greatest_gram[i])):
				assert type(greatest_gram[i]) == tuple
				ngram_string += (' ' + greatest_gram[i][j])
			print("{:d} -- {}".format(greatest, ngram_string))

def main():
	word_list = get_list()
	find_ngram(word_list)

#=================================================================================================
# Function Name:    get_list()
#       Purpose:    call Input() to get innput and call get.wordlist to get the word list.
#					return the wordlist to main.
#    Parameters:    N/A
#       Returns:    list
#=================================================================================================
def get_list():
	get = Input()
	word_list = get.wordlist()
	assert type(word_list) == list
	print(word_list)
	return word_list

#=================================================================================================
# Function Name:    find_ngram()
#       Purpose:    call Ngrams to get user input make a new dict. call process_wordlist to find 
#					how many time each ngrame occurred. call print_max_ngrams in the end to print
#					data out.
#    Parameters:    list
#       Returns:    N/A
#=================================================================================================
def find_ngram(word_list):
	assert len(word_list) >= 0
	n_gram = Ngrams()
	n_gram.process_wordlist(word_list)
	n_gram.print_max_ngrams()


main()
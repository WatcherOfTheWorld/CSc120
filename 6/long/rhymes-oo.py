#=================================================================================================
#   Assignment: Long assignment 6 rhymes-oo.py
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  This file include 2 class and a main program. call WordMap class to init object 
#				 and call readin to read and process input file. init word class with each data in
#				 file. ask user for a input word, find and print all rhymes words.
#=================================================================================================
import sys
#=================================================================================================
# 	 Class Name:    Word
#       Purpose:    make a word object. holding word, pro, prim and data before prim
#=================================================================================================
class Word:
	# init a word object. hold word, pro and compute prim
	def __init__(self, line):
		self._line = line
		self._word = line[0]
		self._pro = line[1:]

		count = 0
		index = 0
		for i in range(0, len(self._pro)):
			# it a word has more than one prim sound, skip the word
			if count > 1:
				print('Error: a word contain more than one prime sound')
				continue
			if self._pro[i][-1] == '1':
				index = i
				count += 1
		# compute prim and data before prim
		self._prim = self._pro[index:]
		self._bef_prim = self._pro[0:index]
		
	# for compare
	def __eq__(self, other):
		other_prim = other.get_prim()
		other_bef_prim = other.get_bef_prim()
		# prim of two word is same and before prim is not same
		if other_prim == self._prim and self._bef_prim != other_bef_prim:
			#return Ture
			return True
		# otherwise return False
		return False

	# get word str
	def get_word(self):
		return self._word

	# get data before prim
	def get_bef_prim(self):
		return self._bef_prim

	# get prim
	def get_prim(self):
		return self._prim

	# return str for print
	def __str__(self):
		return str(self._pro)

#=================================================================================================
# 	 Class Name:    WordMap
#       Purpose:    make a WordMap object. read file and process it. find rhymes word and print 
#					them.
#=================================================================================================
class WordMap:
	# init the object with a dict
	def __init__(self):
		self._pdict = {}

	# ask user for a input file name. read it and process it.
	def read_in(self):
		pfile = input()
		# try if can open the file
		try:
			pfile = open(pfile).readlines()
		# if can not open, print error mess and exit program.
		except IOError:
			print('Error: could not open the file')
			sys.exit(1)
		# otherwise process normally
		for i in range(0, len(pfile)):
			pfile[i] = pfile[i].strip('\n').split()

		self._pfile = pfile
		# creat a dict and map word str to word pro
		pdict = {}
		for i in range(0, len(pfile)):
			if not pfile[i][0] in pdict:
				pdict[pfile[i][0]] = [Word(pfile[i])]
			else:
				pdict[pfile[i][0]].append(Word(pfile[i]))
		self._pdict = pdict

	# ask user for a input word, make it upper case. find the rhymes words and print them
	def find(self):
		word = input()
		word = word.upper()
		# try if word in dict
		try:
			pro = self._pdict[word]
		# if not, print Error and quit app
		except KeyError:
			print('Error: input word in not in dictionary')
			sys.exit(1)

		# make a word list.
		word_list = []

		# looping trough pro of the user input word. find if word in dict have same 
		# pro with input word
		for i in range(0, len(pro)):
			for j in self._pdict:
				for n in range(0, len(self._pdict[j])):
					if self._pdict[j][n] == pro[i]:
						word_list.append(self._pdict[j][n].get_word())

		# looping trough rhymes words list, and print word.
		word_list = list(set(word_list))
		for i in range(0, len(word_list)):
			# if word in word list is input word, do not print it 
			if word_list[i].strip(',.\':;?!@#$%^&*()') == word:
				continue
			print(word_list[i])

	# return dict str for print
	def __str__(self):
		return str(self._pdict)



def main():
	dic = read_infile()
	dic.find()

#=================================================================================================
# Function Name:    read_infile()
#       Purpose:    get a new wordmap object and call read_in to read a file and make a dict.
#    Parameters:    N/A
#       Returns:    dic
#=================================================================================================
def read_infile():
	dic = WordMap()
	dic.read_in()
	return dic


main()
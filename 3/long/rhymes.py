#=================================================================================================
#   Assignment: Long assignment 3
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  This program will input and read a Pronunciation Dictionary file. put all of the
#				 word pronunciation in to a dict. find all the words has same rhyme with user's 
#                input words. and print those words out.
#=================================================================================================
def main():
	pdict = input_file()
	word_list = search(pdict)

#=================================================================================================
# Function Name:    input_file()
#       Purpose:    import a pronunciation Dictionary file and read it into a list. creat a new 
#                   dictionary and maping a list of word's pronunciation to words. return the dict
#			        in the end of this function.
#    Parameters:    N/A
#       Returns:    pdict
#=================================================================================================
def input_file():
	pfile = input()
	pfile = open(pfile).readlines()
	for i in range(0, len(pfile)):
		pfile[i] = pfile[i].strip('\n').split()

	# make a new dict
	pdict ={}
	# looping through every line in pfile and maping proninciation elements to words as key
	for i in range(0,len(pfile)):
		if not pfile[i][0] in pdict:
			pdict[pfile[i][0]] = []
		pdict[pfile[i][0]].append(pfile[i][1:])

	return pdict

#=================================================================================================
# Function Name:    search(pdict)
#       Purpose:    asking user for a word input, make that word upper case and find that word in
#					dict. loop through the pronaciation of that word and find all of other words 
#					that have same rhyming. Save all those words in to a list. Looping through 
#					that list and print all elements in that list out. 
#    Parameters:    pdict
#       Returns:    N/A
#=================================================================================================
def search(pdict):
	word = input()
	word = word.upper()
	pro = pdict[word]
	word_list = []
	# looping through the pronunciation for that word.find the first primary stress in the words
	for i in range(0, len(pro)):
		index_pron = 0
		index = 0
		# find the first primary stress in the words
		for j in range(0, len(pro[i])):
			if pro[i][j][-1] == '1':
				if index_pron == 0:
					index_pron = pro[i][j]
		# find the negitive index for that primary stress
		for j in range(len(pro[i]), 0, -1):
			if index_pron == pro[i][-j]:
				if index == 0:
					index = -j
		# find the words have same rhymes with user input word.
		# put them togeter into a list
		for keys in pdict:
			for k in range(0, len(pdict[keys])):
				if pro[i][index:] == pdict[keys][k][index:]:
					if len(pdict[keys][k]) == len (pro[i][index:]):
						word_list.append(keys)
					elif pro[i][index-1] != pdict[keys][k][index - 1]:
	
						word_list.append(keys)
	# looping through the words list and print them out
	for i in word_list:
		print(i)
					
main()
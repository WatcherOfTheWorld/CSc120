#=================================================================================================
#   Assignment: Long assignment 3
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  This program will fin
#=================================================================================================
def main():
	pdict = input_file()
	word_list = search(pdict)

def input_file():
	pfile = input()
	pfile = open(pfile).readlines()
	for i in range(0, len(pfile)):
		pfile[i] = pfile[i].strip('\n').split()

	pdict ={}
	for i in range(0,len(pfile)):
		if not pfile[i][0] in pdict:
			pdict[pfile[i][0]] = []
		pdict[pfile[i][0]].append(pfile[i][1:])

	return pdict

def search(pdict):
	word = input()
	word = word.upper()
	pro = pdict[word]
	word_list = []
	for i in range(0, len(pro)):
		index_pron = 0
		index = 0
		for j in range(0, len(pro[i])):
			if pro[i][j][-1] == '1':
				if index_pron == 0:
					index_pron = pro[i][j]
		for j in range(len(pro[i]), 0, -1):
			if index_pron == pro[i][-j]:
				if index == 0:
					index = -j

		for keys in pdict:
			for k in range(0, len(pdict[keys])):
				if pro[i][index:] == pdict[keys][k][index:]:
					if len(pdict[keys][k]) == len (pro[i][index:]):
						word_list.append(keys)
					elif pro[i][index-1] != pdict[keys][k][index - 1]:
						word_list.append(keys)

	for i in word_list:
		print(i)
					
main()
wordlist = ['evolve', 'absolve', 'evil', 'absent', 'evidence', 'lake', 'ladder', 'list']
head = 'ev'
# This function find words in a list start with 'head' and return those words
def words_beginning_with(wordlist, head):
	# if tail is a empty str, return orginal list 
	if head =='':
		return wordlist
	# create a new list to contain words start with head.
	word_list = []
	for i in range(0, len(wordlist)):
		if wordlist[i][:len(head)] == head:
			# append that word in to list if it end with head.
			word_list.append(wordlist[i])
	return word_list

words_beginning_with(wordlist, head)
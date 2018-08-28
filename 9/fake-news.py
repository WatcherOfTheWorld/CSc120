#=================================================================================================
#   Assignment: Long assignment 9 fake-news.py
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  This file include 2 class and a main program. one class use to rep a Linked list
#                and one class use to rep node in linked list
#                the main program will read the title in a file.remove any speace and punctuation
#                in title then split them to a list.
#                creat a new LikedList object and add every element in list to LinkedList Obj
#                read in a N. find the count associated with the node in the linked list at 
#`               position n. print every element that has more count then element n
#=================================================================================================
import csv
import string

#=================================================================================================
#    Class Name:    LinkedList
#       Purpose:    repe self._head
#=================================================================================================
class LinkedList:
    # init the class obj, set _head to None 
    def __init__(self):
        self._head = None
    
    # return if self._head is None
    def is_empty(self):
        return self._head == None

    # reutnrn the head 
    def head(self):
        return self._head

    # update the count of word
    # if word is not exist in linked list, add it to linked list
    def update_count(self, word):
        find = self._head
        while find != None:
            # if word has been find in list
            if word == find.word():
                find.incr()
                return
            else:
                find = find.next()
        # add to the list if did not exist
        self.add(Node(word))

    # sort the nodes in the list
    def sort(self):
        # set to_be_sorted to self._head
        to_be_sorted = self._head
        # creat a new LinkedList obj named sorted
        sorted = LinkedList()
        # while there is still to_be_sorted is still has element
        while to_be_sorted != None:
            # make E as the first element that prepair to add
            E  = to_be_sorted
            # set to_be_sorted to be it's next element
            to_be_sorted = to_be_sorted.next()
                    
            curr_element = sorted._head
            # while E has not been add to sorted list
            while E != None:
                # when there is no element in sorted list or 
                # E is large than every element is sorted list
                if curr_element == None:
                    sorted.add(E)
                    E = None
                # when there is more than one elemnt in sotted list
                else:   
                    # if the count of E is less than curr
                    if E.count() <  curr_element.count():
                        # and E is less than next curr element
                        if curr_element._next != None and curr_element._next.count() <= E.count():
                            # insert e after curr_element
                            sorted.insert_after(curr_element, E)
                            E = None
                        # if curr element has no next element
                        elif curr_element._next == None:
                            # insert at the end of the list
                            sorted.insert_after(curr_element, E)
                            E = None

                    # ser curr element to it's next
                    curr_element = curr_element.next()
        # set self._head to sorted list        
        self._head = sorted._head
    
    # add a node to the head of the list
    # from short prob
    def add(self, node):
        node._next = self._head
        self._head = node
        
    # remove a node from the head of the list and return the node
    # from short prob
    def rm_from_hd(self):
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
    
    # insert node2 after node1
    # from short prob
    def insert_after(self, node1, node2):
        assert node1 != None
        node2._next = node1._next
        node1._next = node2

    # get the count at pos n
    def get_nth_highest_count(self, n):
        node = self._head
        while n != 0:
            node = node.next()
            n -= 1

        return node.count()

    # find every element that occered more than n
    # and print those elements out
    def print_upto_count(self, n):
        # creat a new liked list obj
        upto = LinkedList()
        find = self._head
        #if count of element large than n
        while find != None and find.count() >= n:
            temp = find
            #set find to next
            find = find.next()
            # and add that element to new obj
            upto.add(temp)
        upto.sort()

        curr = upto._head
        # when there is element in new linkedlist obj
        while curr != None:
            word = curr.word()
            count = curr.count()
            print("{}:{:d}".format(word, count))
            curr = curr.next()


    # from short prob
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string
#=================================================================================================
#    Class Name:    Node
#       Purpose:    repr self._word, self._count and slef._next
#=================================================================================================
class Node:
    # init the obj
    def __init__(self, word):
        self._word = word
        self._count = 1
        self._next = None
    
    # return the word in str
    def __str__(self):
        return self._word + "; "
    
    # return the word
    def word(self):
        return self._word

    # return the count
    def count(self):
        return self._count

    # set it's next to target
    def set_next(self, target):
        self._next = target

    # incr the count to 1 more
    def incr(self):
        self._count += 1
    
    # return the next element 
    def next(self):
        return self._next


def main():
    cleaned = read_file()
    find(cleaned)
#=================================================================================================
# Function Name:    read_file()
#       Purpose:    read a file, get all of the title in it, remove and speace and punctuation.
#                   add them to a list
#    Parameters:    N/A
#       Returns:    clearned
#=================================================================================================
def read_file():
    file_name = input('File:')
    # try to open the file
    try:
        lines = open(file_name)
    # if falled, quit
    except IOError:
        print("ERROR: Could not open file " + file_name)
        exit(1)
    # use csv module to read file
    csvreader = csv.reader(lines)
    # creat a empty str to add title in file
    title = ''
    # set i = 0 
    i = 0
    for itemlist in csvreader:
        # if at first line
        if i == 0:
            i += 1
            # has str is 'title'
            if itemlist[4] == 'title':
                # do not add it
                continue
        # add the reset of lowered titles
        title += itemlist[4].lower()
        # and a whitespece to split from every title
        title += ' '

    # usr string module to get whitespace and punctation str in a list
    clean = list(string.whitespace)
    clean.extend(list(string.punctuation))

    # for every needs to be cleaned element
    for i in range(0, len(clean)):
        # replace the element to ' '
        title = title.replace(clean[i], ' ')
    # and splite them to a list by ' '
    cleaned = title.split()
    # set  i = 0
    i = 0
    # while i is large than len of cleaned list
    while i < len(cleaned):
        # if the len of that element less than 2
        if len(cleaned[i]) <= 2:
            #del it
            del cleaned[i]
            # decr i to 1
            i -= 1
        i += 1

    return cleaned

#=================================================================================================
# Function Name:    find()
#       Purpose:    take cleaned from main. creat a liked list obj, add every element from cleaned 
#                   ro word linked list
#                   ask user for a N number,and find the count associated with the node in the 
#                   linked list at position n. print every element that has more count then 
#                   element n
#    Parameters:    cleaned
#       Returns:    N/A
#=================================================================================================
def find(cleaned):
    word = LinkedList()
    for i in range(0, len(cleaned)):
        word.update_count(cleaned[i])
    
    # try to read user input in int
    try:
        N = int(input('N: '))
    # if can not covert to int 
    except ValueError:
        print("ERROR: Could not read N")
        # quit
        exit(1)

    # make sure N is not less than 0
    assert N >= 0

    # sort the word
    word.sort()
    # get the element count at N pos
    k = word.get_nth_highest_count(N)
    # find every element has more than k count, and print them out
    word.print_upto_count(k)


main()
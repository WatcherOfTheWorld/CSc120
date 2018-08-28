#=================================================================================================
#   Assignment: Long assignment 10 friends.py 　　　　　　　　　　　　　　　　　
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  import linked_list from outer file. readin a file has firend info. process it to 
#                a list. take the list, for each name creat a node obj. each node obj has a list 
#                indict his friends. read in two name. find the people is firend of that both 2 
#                name
#=================================================================================================
from linked_list import *
def main():
    lines = read()
    find(lines)

#=================================================================================================
# Function Name:    read()
#       Purpose:    read a file, get all of the name in it, remove and speace and spece.
#                   add them to a list
#    Parameters:    N/A
#       Returns:    lines
#=================================================================================================
def read():
    name = input('Input file: ')
    # try to open file
    try: 
        lines = open(name).readlines()
    # failed, print error and quit
    except IOError:
        print("ERROR: Could not open file " + name)
        exit(1)

    # for each line, strip usless info and split into list of list
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip('\n').split()
    
    return lines

#=================================================================================================
# Function Name:    find()
#       Purpose:    creat linkedlist obj. for each name creat a node. for each node, append their 
#                   friend to the linked list in the node. ask user for two name and find people
#                   who is friend of that two name.
#    Parameters:    lines
#       Returns:    N/A
#=================================================================================================
def find(lines):
    friend_list = LinkedList()
    temp = []
    # get all the name
    for i in range(0, len(lines)):
        temp += lines[i]
    friend_set = list(set(temp))

    # creat node for each name
    for i in range(0 ,len(friend_set)):
        friend_list.add(Node(friend_set[i]))

    # append friend's name node for each node 
    for i in range(0, len(lines)):
        node = friend_list.find(lines[i][0])
        node.add(Node(lines[i][1]))
        node = friend_list.find(lines[i][1])
        node.add(Node(lines[i][0]))

    name1 = input('Name 1: ')
    name2 = input('Name 2: ')
    people = friend_list.find_both(name1, name2)
    for i in range(0, len(people)):
        print(people[i])
 
main()
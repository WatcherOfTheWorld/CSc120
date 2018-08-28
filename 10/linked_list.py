#=================================================================================================
#    Class Name:    LinkedList
#       Purpose:    repe self._head
#=================================================================================================
class LinkedList:
    # init the class obj, set _head to None 
    def __init__(self):
        self._head = None

    # add a node to the head of the list
    def add(self, name):
        name._next = self._head
        self._head = name
    
    # get name1 and name2 and call find to find driend of name1 and name 2
    # get the name that both from firend 1 and friend 2
    def find_both(self, name1, name2):
        friend1 = self.find(name1)
        friend2 = self.find(name2)
        element = friend1._head
        both_friend = []
        while element != None:
            key = friend2._head
            while key != None:
                # if element in friend1 is in friend2
                if element._name == key._name:
                    # add the name to friend list
                    both_friend.append(key._name)
                key = key.next()
            element = element.next()
        return both_friend
    
    # return the firend of name
    def find(self, name):
        cur = self._head
        while cur != None:
            if cur._name == name:
                return cur.get_friend()
            cur = cur.next()
        assert cur != None
    
    # str methond
    def __str__(self):
        string = '[ '
        cur_node = self._head
        while cur_node != None:
            string += str(cur_node)
            cur_node = cur_node.next()
        string += ']'
        return string
        
#=================================================================================================
#    Class Name:    Node
#       Purpose:    repr self._word, self._count and slef._next
#=================================================================================================    
class Node:
    # init the obj
    def __init__(self, name):
        self._name = name
        self._next = None
        self._friend = LinkedList()
    
    # add a friend node to list
    def add(self, node):
        self._friend.add(node)
    
    # return the friend list
    def get_friend(self):
        return self._friend

    # return the next node
    def next(self):
        return self._next

    # return the word in str    
    def __str__(self):
        return self._name + '; '+ str(self._friend)
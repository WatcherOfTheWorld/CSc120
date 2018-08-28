#=================================================================================================
#   Assignment: Long assignment 11 huffman.py 　　　　　　　　　　　　　　　　　
#       Author: Feiran Yang 
#
#       Course:  CS 120
#   Instructor:  Saumya Debray
#
#  Description:  read a file, creat a tree and decoded value in the tree
#=================================================================================================


# this class rep a BinartSearchTree Obj
class Node:
    # init a node
    def __init__(self,value):
        self._root = value  
        # left tree
        self._left = None
        # right tree
        self._right = None  
    
    # add value to the tree
    def add(self, node, dirc):
        if dirc != -1:
            # if node should be left tree
            if dirc == 0:
                # set it's previues tree' left
                self._left = node
            # otherwise right
            else:
                self._right = node


def main():
    preorder, inorder, encoded = read()
    tree = build(preorder, inorder)
    get_post(tree)
    decoded(tree,encoded)

#=================================================================================================
# Function Name:    read()
#       Purpose:    read a file, get 3 lines of data from it
#    Parameters:    N/A
#       Returns:    preorder, inorder, encoded
#=================================================================================================
def read():
    file = input('Input file: ')
    try:
        lines = open(file).readlines()
    except IOError:
        print('ERROR: Counld not open file '+ file)
        exit(1)
    
    preorder = lines[0].split()
    inorder = lines[1].split()
    string = ''
    # del space in number
    for i in range(0, len(inorder)):
        string += inorder[i]
    inorder = string
    encoded = lines[2].strip()
    return preorder, inorder, encoded

#=================================================================================================
# Function Name:    build()
#       Purpose:    build a tree
#    Parameters:    preorder, inorder
#       Returns:    tree 
#=================================================================================================
def build(preorder, inorder):
    # creat a tree with first number in preorder
    tree = Node(int(preorder[0]))
    left, right = inorder.split(preorder[0])
    add(tree, preorder[1:], left, right)
    return tree

#=================================================================================================
# Function Name:    add()
#       Purpose:    add a node to the tree to the right pratent.
#    Parameters:    tree, preorder, left, right
#       Returns:    lines
#=================================================================================================
def add(tree, preorder, left, right):
    temp = tree
    # creat a new node 
    root = Node(int(preorder[0]))
    # if in left
    if preorder[0] in left:
        # add it to left
        temp.add(root,0)
        # split by that number
        sub_left, sub_right = left.split(preorder[0])
        preorder = preorder[1:]
        # call this function again to add it's child
        preorder = add(temp._left, preorder, sub_left, sub_right)

        # add rest of child in right
        node = Node(int(right[0]))
        temp.add(node,1)
        if len(right) > 1:
            sub_left, sub_right = right.split(preorder[0])
            temp_order = preorder[0]
            preorder = preorder[1:]
            add(temp._right, preorder, sub_left, sub_right)
            temp._right._root = int(temp_order)

    elif preorder[0] in right:
        # add to right 
        temp.add(root,1)
        # split by it's value
        sub_left, sub_right = right.split(preorder[0])
        preorder = preorder[1:]
        # add child
        preorder = add(temp._right, preorder, sub_left, sub_right)

        # add child in left
        node = Node(int(left[0]))
        temp._left.add(node,1)
        if len(left) > 1:
            sub_left, sub_right = left.split(preorder[0])
            temp_order = preorder[0]
            preorder = preorder[1:]
            add(temp._left, preorder, sub_left, sub_right)
            temp._left._root = int(temp_order)

    return preorder

#=================================================================================================
# Function Name:    get post()
#       Purpose:    get tree in main, print value in postorder
#    Parameters:    tree
#       Returns:    N/A
#=================================================================================================
def get_post(tree):
    post = find_post(tree)
    post = break_down(post)
    # print every value in tree
    for i in range(0,len(post)):
        print(str(post[i])+' ',end='')
    print()

#=================================================================================================
# Function Name:    find post()
#       Purpose:    find the value in postorder
#    Parameters:    tree
#       Returns:    N/A
#=================================================================================================
def find_post(tree):
    temp = tree
    post = []
    # if not child
    if temp._left == None and temp._right == None:
        # return it's self
        return temp._root
    # if only one child
    if temp._left != None:
        temp_left = temp._left
        post.append(find_post(temp_left))
    if temp._right != None:
        temp_right = temp._right
        post.append(find_post(temp_right))
    # append value to list
    post.append(temp._root)
    return post

#=================================================================================================
# Function Name:    break_down()
#       Purpose:    get post order list of list, break them into one list
#    Parameters:    post
#       Returns:    N/A
#=================================================================================================
def break_down(post):
    postes = []
    # add element to list
    for i in range(0, len(post)):
        # if that element is a list
        if type(post[i]) == list:
            # breal that list down
            for j in range(0,len(post[i])):
                # add to list
                postes.append(post[i][j])
        else:
            postes.append(post[i])
    # if there is still one or more list in list
    for i in range(0, len(postes)):
        if type(postes[i]) == list:
            # break it down
            postes = break_down(postes)
            break
    return postes
    
        
#=================================================================================================
# Function Name:    decoded()
#       Purpose:    print decoded value
#    Parameters:    tree, encoded
#       Returns:    N/A
#=================================================================================================
def decoded(tree,encoded):
    decode = ''
    # still element in encoded list
    while len(encoded) > 0:
        # call decoding to get updated encoded list and decoded number
        pre, encoded = decoding(tree, encoded)
        # add decoded number value to str
        decode += str(pre)
    print(decode)

#=================================================================================================
# Function Name:    read()
#       Purpose:    take tree,encoded to find a decoded number.
#    Parameters:    tree,encoded
#       Returns:    N/A
#=================================================================================================
def decoding(tree,encoded):
    temp = tree
    # while temp is a child
    while temp != None:
        pre = temp._root
        if len(encoded) > 0:
            # if first value of encoded str is 0
            if encoded[0] == '0':
                # navigate to it's left
                temp = temp._left
            else:
                temp = temp._right
        else:
            temp = None
        
        if temp == None:
            continue
        encoded = encoded[1:]
    return pre,encoded
    

main() 
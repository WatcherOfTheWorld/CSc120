def concat_elements(list, startpos, stoppos):
    # determine the range
    if startpos <=0 :
        startpos = 0
    if stoppos + 1 >= len(list):
        stoppos = len(list) - 1
    
    word = ""
    #iterating over the list, and add evey element in the range to a str
    for i in range(startpos, stoppos + 1):
        word += list[i]
    
    return (word)
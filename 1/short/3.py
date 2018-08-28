def concat_elements(list, startpos, stoppos):
    if startpos <=0 :
        startpos = 0
    if stoppos+1 >= len(list):
        stoppos = len(list) - 1
    
    word = list[startpos: stoppos]
    word = ''.join(word)

    return word


concat_elements(['aa','bb','cc','dd'], 1, 3)
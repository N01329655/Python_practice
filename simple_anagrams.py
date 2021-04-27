def anagrams(word,words):
    res = [] ## used to store sorted string 
    result = [] ## used to save result 
    to_compare = ''.join(sorted(word)) ## to sort string and then use it to compare
    counter = 0
    
    for word1 in words:
        res.append(''.join(sorted(word1)))
    
    for word_ in res:
        if to_compare == word_:
            result.append(words[counter])
        counter +=1 
                
            
    return result

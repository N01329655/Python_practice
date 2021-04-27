def duplicate_encode(word):
    res_word = "" # used to record result string 
    list1 = list(word.lower()) # separating string into list
    n = 0 # used to loop through list
    j = 0
    counter = 0  # used to find unique elements 
    while n < len(list1):
        to_check = list1[n] # start with first character 
        while j < len(list1):
            if to_check == list1[j]:
                counter = counter + 1 # adding 1 if we find a match
            j = j + 1
        if counter > 1 :   ## we have to find more than 1 match beause one time we compare it with itself!
            res_word = res_word + ")"
        else: ## if counter == 1 wich means we find itself then we assing ( as for unique values 
            res_word = res_word + "("
            
        n = n + 1
        ## reseting all neccessary counters
        j = 0
        counter = 0
            
    return res_word
        
            
             
res = duplicate_encode("Success")
print(res)

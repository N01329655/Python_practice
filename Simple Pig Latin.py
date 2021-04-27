def pig_it(text):
    list1 = list(text.split(" ")) # separating the text into an array of strings ['My','frined',....]
    res_string = "" # string to store the result 
    list2 = ['[','@','_','!','#','$','%','^','&','*','()','<>','?','/','|','}','{','~',':',']','\\']
    for word_ in list1:
        # print(word_)
        ## check for single characters such as: !, :, ., ....
        if word_ in list2:
            res_string = res_string + word_ + " " 
        else:
            
            ## spliting each word into a new array of characters Ex: ['d','e','a','r']                 
            temp_list = list(word_)
            #if temp_list
            first_symbol = temp_list[0]
            ## removing first symbol and adding it to the back 
            temp_list.remove(first_symbol)
            temp_list.append(first_symbol)
            ## adding ay to the end of each word 
            lenght = len(temp_list)
            if temp_list[lenght-1] != " ":
                temp_list.append("ay")
                ## merging strings from list into one string
            for str1 in temp_list:
                res_string = res_string + str1
                
            res_string += " "
        
        
        
    return(res_string.strip())

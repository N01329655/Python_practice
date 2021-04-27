def validBraces(string):
    result = False ## declaring the returning value boolean (True/ False)
    valid_list = ['()','{}','[]'] ## validation list 
    input_list = list(string) ## spliting a string into list ['(',')','{','{',.....]
    counter = 2 ## used for first condtion 
    lenght = len(input_list)
    ##checking firts condition if (),[],{}
    f_cond = input_list[0] + input_list[1]
    ##checking the last elements if () [] {}
    f_cond2 = input_list[lenght-2] + input_list[lenght-1]
    
    
    if (f_cond in valid_list) & (f_cond2 not in valid_list): ##checking firts condition if (),[],{}
        while counter < lenght-1: ## used to stop looping before reaching the last element
            f_cond = input_list[counter] + input_list[counter+1]
            
            if f_cond in valid_list:
                counter +=2
            else: ## if we have any mismatch instantly return false
                return False
        return True     
    
    elif (f_cond in valid_list) & (f_cond2 in valid_list):
        midd_pos = int((lenght / 2) - 1) ## to get mid position
        counter_forward = midd_pos +1    ## used to loop forward        
        for lop in range(midd_pos,lenght-1): ## to loop we use the exact number of pairs 
            f_cond = input_list[midd_pos] + input_list[counter_forward]
            ## our counters should never reach penultimate(предпоследний)
            if counter_forward == lenght - 2:
                break
            if f_cond in valid_list:
                midd_pos -=1        ## to move position backward 
                counter_forward +=1  ## to move position forward 
            else:
                return False
            
            return True 

    else:
        ## *** to enter the loop we have to have an even number of elements **** important 
        if lenght % 2 != 0:
            return False
            
        else:
            midd_pos = int((lenght / 2) - 1) ## to get mid position
            counter_forward = midd_pos +1    ## used to loop forward        
            for lop in range(midd_pos,lenght-1): ## to loop we use the exact number of pairs 
                f_cond = input_list[midd_pos] + input_list[counter_forward]
                if f_cond in valid_list:
                    midd_pos -=1        ## to move position backward 
                    counter_forward +=1  ## to move position forward 
                else:
                    return False
            
            return True 

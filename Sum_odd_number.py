def row_sum_odd_numbers(n):
    secondary_counter = n # used in last loop
    result = 0
    counter = 0
    starting_number = 1 # used to start calculating the result 
    while n != 1: # loop to get the exact number of digits which are located right before the digit we will use to start our calculations
        counter = counter + (n-1)
        n -= 1  
    while counter > 0 :
        starting_number = starting_number + 2
        counter -= 1
    # print(starting_number)
    ## know we have everything to find the result
    result = starting_number
    while secondary_counter > 1:
        starting_number = starting_number + 2
        result = result + starting_number
        secondary_counter -= 1
    
    return result

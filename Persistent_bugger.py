counter = 0 ## used to count the number times that recursion takes place
def persistence(n):
    result = 1
    global counter 
    ## first condtion for every digit
    if n <=9:
        return 0
    else:
        # split a nubmer into a list of digits 
        list_digits = list(map(int,str(n)))
        for num in list_digits:
            result = result * num
        counter +=1
        print(result)
        if result <=9:
            counter_res = counter 
            counter = 0
            return counter_res
        else: 
            return persistence(result)

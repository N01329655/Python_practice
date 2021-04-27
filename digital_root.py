def digital_root(n):
	num_str = str(n) # converting num to string
	list_str_nums = list(num_str) # a list of stings ['1','2'....]
	total_sum = 0
	
	for str_num in list_str_nums:
		total_sum = total_sum + int(str_num) # converting and adding 1 + 2 + 3....
	# required check for the amount of digits in a number
	check_str = list(str(total_sum)) # should be check_str = [1,2,3,....]	
	if len(check_str) < 2:
		return total_sum
	else:
		return digital_root(total_sum)
		

def unique_in_order(iterable):
	result = []
	if isinstance(iterable,str): ## to check what we receive a string or a list
		temp_list = list(iterable)
		
	temp_list = iterable
	counter = len(temp_list) - 1 
	for num in range(0,len(temp_list)):

		if  counter == num :
			result.append(temp_list[num])
			break
					
		if temp_list[num] == temp_list[num+1]:
			pass
				
		else:
			result.append(temp_list[num])
					
	return result
				
				
print(unique_in_order([1,1,1,2,2,3,3,4,5,6,66,77,77,77,9,9,9]))
print(unique_in_order("AABBAFFEddDSuccess"))



def get_pins(observed):
	
	
	res_list= []
	## all possible combinations for each number plus **itself:
	poss_comb = { 0 : [8,0],
				  9 : [6,8,9],
				  8 : [0,7,9,5,8],
				  7 : [8,4,7],
				  6 : [3,5,6,9],
				  5 : [8,6,4,2,5],
				  4 : [7,5,1,4],
				  3 : [2,3,6],
				  2 : [5,3,1,2],
				  1 : [4,2,1],
				  } 
				 
	input_pin = list(observed)
	'''c = "0"
	c1 = "00"
	c2 = "000"
	c3 = "0000"
	if(observed == c or  observed == c1 or observed == c2 or observed == c3): 
		return list(observed)
		'''
	
		
		
	
	
	
	if len(observed) == 1:
		
		for item in poss_comb[int(observed)]:
			res_list.append(str(item))		
		
		return res_list
	
	
		
	if len(input_pin) == 2:
			list1 = poss_comb[int(input_pin[0])]
			list2 = poss_comb[int(input_pin[1])]
			temp1 = ''
			temp2 = ''
			for val1 in list1:
				temp1 = str(val1)
				for val2 in list2:
					temp2 = temp1 + str(val2)
					res_list.append(temp2)
			
	if len(input_pin) == 3:
			list1 = poss_comb[int(input_pin[0])]
			list2 = poss_comb[int(input_pin[1])]
			list3 = poss_comb[int(input_pin[2])]
			temp1 = ''
			temp2 = ''
			temp3 = ''
			for val1 in list1:
				temp1 = str(val1)
				for val2 in list2:
					temp2 = temp1 + str(val2)
					for val3 in list3:
						temp3 = temp2 + str(val3)
						res_list.append(temp3)
						
						
			
	if len(input_pin) == 4:
			list1 = poss_comb[int(input_pin[0])]
			list2 = poss_comb[int(input_pin[1])]
			list3 = poss_comb[int(input_pin[2])]
			list4 = poss_comb[int(input_pin[3])]
			temp1 = ''
			temp2 = ''
			temp3 = ''
			temp4 = ''
			for val1 in list1:
				temp1 = str(val1)
				for val2 in list2:
					temp2 = temp1 + str(val2)
					for val3 in list3:
						temp3 = temp2 + str(val3)
						for val4 in list4:
							temp4 = temp3 + str(val4)
							res_list.append(temp4)
	if len(input_pin) == 5:
			list1 = poss_comb[int(input_pin[0])]
			list2 = poss_comb[int(input_pin[1])]
			list3 = poss_comb[int(input_pin[2])]
			list4 = poss_comb[int(input_pin[3])]
			list5 = poss_comb[int(input_pin[4])]
			temp1 = ''
			temp2 = ''
			temp3 = ''
			temp4 = ''
			temp5 = ''
			for val1 in list1:
				temp1 = str(val1)
				for val2 in list2:
					temp2 = temp1 + str(val2)
					for val3 in list3:
						temp3 = temp2 + str(val3)
						for val4 in list4:
							temp4 = temp3 + str(val4)
							for val5 in list5:
								temp_5 = temp4 + str(val5)
								res_list.append(temp_5)
	if len(input_pin) == 6:
			list1 = poss_comb[int(input_pin[0])]
			list2 = poss_comb[int(input_pin[1])]
			list3 = poss_comb[int(input_pin[2])]
			list4 = poss_comb[int(input_pin[3])]
			list5 = poss_comb[int(input_pin[4])]
			list6 = poss_comb[int(input_pin[5])]
			temp1 = ''
			temp2 = ''
			temp3 = ''
			temp4 = ''
			temp5 = ''
			temp6 = ''
			for val1 in list1:
				temp1 = str(val1)
				for val2 in list2:
					temp2 = temp1 + str(val2)
					for val3 in list3:
						temp3 = temp2 + str(val3)
						for val4 in list4:
							temp4 = temp3 + str(val4)
							for val5 in list5:
								temp5 = temp4 + str(val5)
								for val6 in list6:
									temp6 = temp5 + str(val6)
									res_list.append(temp6)
	if len(input_pin) == 7:
			list1 = poss_comb[int(input_pin[0])]
			list2 = poss_comb[int(input_pin[1])]
			list3 = poss_comb[int(input_pin[2])]
			list4 = poss_comb[int(input_pin[3])]
			list5 = poss_comb[int(input_pin[4])]
			list6 = poss_comb[int(input_pin[5])]
			list7 = poss_comb[int(input_pin[6])]
			temp1 = ''
			temp2 = ''
			temp3 = ''
			temp4 = ''
			temp5 = ''
			temp6 = ''
			temp7 = ''
			for val1 in list1:
				temp1 = str(val1)
				for val2 in list2:
					temp2 = temp1 + str(val2)
					for val3 in list3:
						temp3 = temp2 + str(val3)
						for val4 in list4:
							temp4 = temp3 + str(val4)
							for val5 in list5:
								temp5 = temp4 + str(val5)
								for val6 in list6:
									temp6 = temp5 + str(val6)
									for val7 in list7:
										temp7 = temp6 + str(val7)
										res_list.append(temp7)		
	if len(input_pin) == 8:
			list1 = poss_comb[int(input_pin[0])]
			list2 = poss_comb[int(input_pin[1])]
			list3 = poss_comb[int(input_pin[2])]
			list4 = poss_comb[int(input_pin[3])]
			list5 = poss_comb[int(input_pin[4])]
			list6 = poss_comb[int(input_pin[5])]
			list7 = poss_comb[int(input_pin[6])]
			list8 = poss_comb[int(input_pin[7])]
			temp1 = ''
			temp2 = ''
			temp3 = ''
			temp4 = ''
			temp5 = ''
			temp6 = ''
			temp7 = ''
			temp8 = ''
			for val1 in list1:
				temp1 = str(val1)
				for val2 in list2:
					temp2 = temp1 + str(val2)
					for val3 in list3:
						temp3 = temp2 + str(val3)
						for val4 in list4:
							temp4 = temp3 + str(val4)
							for val5 in list5:
								temp5 = temp4 + str(val5)
								for val6 in list6:
									temp6 = temp5 + str(val6)
									for val7 in list7:
										temp7 = temp6 + str(val7)
										for val8 in list8:
											temp8 = temp7 + str(val8)
											res_list.append(temp8)				
	
	return res_list
	
res = get_pins('23450677')
print(res)

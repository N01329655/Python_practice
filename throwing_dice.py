'''
def score(dice):
	scoring_board = {1000 :	3, ## for 3 ones   do it with all dics
					 600: 18, ## for 3 sixs
					 500: 15, ## for 3 fives
					 400: 12, ## for 3 fourths
					 300:  9, ## for 3 threes 
					 200:  6, ## for 3 twos
					 100:  1, ## for 1 
					 50:  5,} ## for 5 
	temp_cal = [0,0,0,0,0,0]			 
	total_score = 0
	for num in range(0,5):
		if dice[num] == 1:
			temp_cal[0] = temp_cal[0] + dice[num] 
		elif dice[num] == 2:
			temp_cal[1] = temp_cal[1] + dice[num]
		elif dice[num] == 3:
			temp_cal[2] = temp_cal[2] + dice[num]	
		elif dice[num] == 4:
			temp_cal[3] = temp_cal[3] + dice[num]
		elif dice[num] == 5:
			temp_cal[4] = temp_cal[4] + dice[num]
		elif dice[num] == 6:
			temp_cal[5] = temp_cal[5] + dice[num]
	
	for num in range(0,6):
		if temp_cal[0]  scoring_board[1000] == 0:
			result = result + 1000
		elif
				
				

	print(temp_cal)
				
	return total_score


score([1,1,1,0,0])
'''




def score(dice):
	result = 0	  
	temp_cal = 	{ 		  'sixs':0 ,
						  'fives':0 , 
						  'fourths':0 ,
						  'threes':0  , 
						  'twos':0 ,
						  'ones':0,  }
	
						  
	for num in range(0,5):
				if dice[num] == 1:
					temp_cal['ones'] = temp_cal['ones'] + 1
					
				elif dice[num] == 2:
					temp_cal['twos'] = temp_cal['twos'] + 2
					
				elif dice[num] == 3:
					temp_cal['threes'] = temp_cal['threes'] + 3
					
				elif dice[num] == 4:
					temp_cal['fourths'] = temp_cal['fourths'] + 4
				
				elif dice[num] == 5:
					temp_cal['fives'] = temp_cal['fives'] + 5
				
				elif dice[num] == 6:
					temp_cal['sixs'] = temp_cal['sixs'] + 6
			
	for key in temp_cal.keys():
				if key == 'ones':
					reminder = temp_cal[key] % 3
					if temp_cal[key] >= 3:
						result = result + 1000
						result = result + (reminder * 100)
					else:
						result = result + (reminder * 100)
						
				if key == 'twos':
					if temp_cal[key] >= 6:
						result = result + 200
						
				if key == 'threes':
					if temp_cal[key] >=9:
						result = result + 300
						
				if key == 'fourths':
					if temp_cal[key] >=12:
						result = result + 400
						
				if key == 'fives':
					reminder = temp_cal[key] % 3
					if temp_cal[key] == 10:
						result = result + 50 *2
					elif temp_cal[key] == 5:
						result = result + 50
						
					else:
						result = result + 500
						if reminder == 2:
							result = result + 50
						else:
							result = result + (50 * 2)
					

					
				if key == 'sixs':
					if temp_cal[key] >= 18:
						result = result + 600

	return result
	
	
print(score([5,3,2,4,5]))
						
					
				
					 
	
	
	

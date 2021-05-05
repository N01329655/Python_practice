''' 
short description 
	 mathematics, a perfect power is a positive integer that
	 can be expressed as an integer power of another positive integer.
	 Ex: n is a perfect power if there exist numbers m > 1 and k >1 
	 that m^k = n
	 ## 
	 Ex: input 9 output should be: [3,2]
	 knowing the property of logarithms I used the following algorythm
	 log(9,(Base m)) = k
	 I compare if k > 1 and m > 1
	  then check k to be an integer:
	  if true 
	  return [m,k]
	  else
	  increase Base(m) by one 
	  
	  But my code doesn't pass all tests on code wars 
	  I haven't figured it out yet 
	  why it is so


'''
import math
import time 
def isPP(n):
	condition = 1
	result = []
	m = 2
	
	while condition != None:
		k = math.log(n,m)
	
		if k > 1 and m > 1:
			if  k.is_integer():
				result.append(m)
				result.append(int(k))
				return result
		if m > n:
			return None
		m +=1
		
		
	
print(isPP(9))
	
	

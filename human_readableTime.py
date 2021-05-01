def make_readable(seconds):
	res = ''
	if seconds <= 59:
		if seconds < 10:
			res = '00:' + '00:' + '0'+str(seconds) 
			return res
		else:
			res = '00:' + '00:' +str(seconds) 
			return res
	
	else:
		hours = int(seconds / 3600)
		remained_secs = seconds % 3600
		if hours < 10:
			res =  "0" + str(hours) + ":"
		else:
			res =  str(hours) + ":"
			
		minutes = int(remained_secs / 60)
		remained_secs = remained_secs % 60
		if minutes < 10:
			res = res+  "0" + str(minutes) + ":"
		else:
			res =  res + str(minutes) + ":"
		
		if remained_secs < 10:
			res = res+  "0" + str(remained_secs)
		else:
			res =  res + str(remained_secs)
	
				
	
	
	return res
	
	


print(make_readable(0))
print(make_readable(5))
print(make_readable(80))
print(make_readable(86399))
print(make_readable(359999))
print(make_readable(3600))









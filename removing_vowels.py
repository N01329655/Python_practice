
def disemvowel(string_):
	to_remove = "aeuio"
	for char_to_remove in to_remove:
		string_ = string_.replace(char_to_remove,"")
	return string_    
 
result = disemvowel("This website is for losers LOL!!")
print(result)


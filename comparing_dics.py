def cakes(recipe,available):
	result = 0
	total_amount_ofCakes = []
	temp_res = 0
	## if we dont have at least one ingriedent in available return 0!!
	for key in recipe.keys():     ##cakes({flour: 500, sugar: 200, eggs: 1},
		if key in available.keys():			##{flour: 1200, sugar: 1200, eggs: 5, milk: 200})
			total_amount_ofCakes.append(int(available[key]/recipe[key]))
		else:
			return 0
			
	result = min(total_amount_ofCakes)
	return result 


print(cakes({"flour": 500, "sugar": 200, "eggs": 1},{"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))

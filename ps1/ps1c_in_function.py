def part_c(initial_deposit):
	#########################################################################
	cost_of_dream_home = 800000
	portion_down_payment = 0.25
	r = 1
	lower = 0
	higher = 1
	months = 36
	amount_saved = initial_deposit * (1 + r / 12) ** months
	steps = 0
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	if amount_saved < cost_of_dream_home * portion_down_payment:
	    r = None
	else:
	    while abs(amount_saved - cost_of_dream_home * portion_down_payment) > 100:
	        if amount_saved >= cost_of_dream_home * portion_down_payment:
	            higher = r
	            r = (lower + r) / 2
	        else:
	            lower = r
	            r = (r + higher) / 2
	        amount_saved = initial_deposit * (1 + r / 12) ** months
	        steps += 1
	
	print(f"Best saving rates: {r}")
	print(f"Steps in bisection search: {steps}")
	return r, steps
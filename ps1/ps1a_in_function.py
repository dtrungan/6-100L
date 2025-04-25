def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	portion_down_payment = 0.25
	amount_saved = 0
	r = 0.05
	months = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while amount_saved <= cost_of_dream_home * portion_down_payment:
	    amount_saved *= 1 + r / 12
	    amount_saved += yearly_salary / 12 * portion_saved
	    months += 1
	
	print(f"Number of months: {months}")
	return months
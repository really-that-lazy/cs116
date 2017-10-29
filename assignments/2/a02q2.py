## Question 2
import check

## interest_rate takes a numeric balance for an account, along with a type and
## level as strings which describe the minimum balances they require to 
## accumulate interest, and the interest rates that they can  accumulate

## interest_rate: Nat Str Str -> Nat

## ie interest_rate(2200, "Personal", "Standard") => 1.2

def interest_rate(balance, account_type, level):
	if(account_type == "Personal"):
		if(level == "Gold"):
			if(balance < 2000):
				return 0.0
			elif(balance < 5000):
				return 1.9
			else:
				return 2.3
		else:
			return 1.2
	elif(account_type == "Business"):
		if(level == "Standard"):
			if(balance < 2500):
				return 0.0
			else:
				return 1.75
		elif(level == "Platinum"):
			if(balance < 10000):
				return 0.0
			else:
				return 2.6
    
    
if(__name__ == "__main__"):

	check.expect("interest_rate(4500, 'Personal', 'Gold')", interest_rate(4500, 'Personal', 'Gold'), 1.9)
	check.expect("interest_rate(6000, 'Personal', 'Standard')", interest_rate(6000, 'Personal', 'Standard'), 1.2)	
	check.expect("interest_rate(500.56, 'Personal', 'Gold')", interest_rate(500.56, 'Personal', 'Gold'), 0)
	check.expect("interest_rate(-6000, 'Business', 'Standard')", interest_rate(-6000, 'Business', 'Standard'), 0)
	check.expect("interest_rate(2999, 'Business', 'Standard')", interest_rate(2999, 'Business', 'Standard'), 1.75)
	check.expect("interest_rate(2999, 'Business', 'Platinum')", interest_rate(2999, 'Business', 'Platinum'), 0.0)
	check.expect("interest_rate(12999, 'Business', 'Standard')", interest_rate(12999, 'Business', 'Platinum'), 2.6)

## Question 1
import check

## parking_costs consumes two parameters describing the timescale that the
## charge is being assessed for, and the actual amount of time being charged for

## for short_term = True, (less than one day), the cost is 4$ for each 20
## minutes used, full or partial, up to a maximum cost of 28$ per day

## for short_term = False, (longer than one day), the cost is 28$ for each day,
## up to a maximum cost of 120$ for the week, each additional week being charged
## the same way

## parking_costs: Bool Nat -> Nat

def parking_costs(short_term, time):
	if(time == 0):
		return 0.0
	else:
		if(short_term):
			days = time//(60*24) + 1
			## plus one because days are rounded up here
			if(days > 1):
				return parking_costs(False, days)
			
			timeBlocksConsumed = (time//20)+1
			##print "timeBlocksConsumed=%i" % timeBlocksConsumed
			if(timeBlocksConsumed >= 7):
				return 28
			else:
				return 4*timeBlocksConsumed
			
		else:
			weeks = time//7
			days = time-(7*weeks)
			
			if(days >= 5):
				days = 0
				weeks += 1
			return ((weeks*120) + (days*28))
	
	

if(__name__ == "__main__"):

	check.expect("parking_costs(True, 0)", parking_costs(True, 0), 0)
	## did not spend any time at all parked, no cost

	check.expect("parking_costs(True, 2)", parking_costs(True, 2), 4)
	## parked for 2 minutes, so round up to 20 minutes, 1x20 minutes
	
	check.expect("parking_costs(True, 47)", parking_costs(True, 47), 12)
	## parked for 47 minutes, so round up to 60 minutes, 3x20 minutes
	
	check.expect("parking_costs(True, 500)", parking_costs(True, 500), 28)
	## parked for 500 minutes, past the cutoff of 140 minutes, 28$ for the day
	## max, so round to 28$

	check.expect("parking_costs(True, 1500)", parking_costs(True, 1500), 56)
	## parking time in minutes exceeds one full day, so the function gets
	## recalled with the appropriate number of days
	
	check.expect("parking_costs(False, 0)", parking_costs(False, 0), 0)
	## parked for 0 days, no cost
	
	check.expect("parking_costs(False, 2)", parking_costs(False, 2), 56)
	## parked for 2 days, 28x2 = 56$

	check.expect("parking_costs(False, 6)", parking_costs(False, 6), 120)
	## parked for 6 days, past the max for the week, 6*28=168 is over 120$, so
	## it gets rounded down to 120$

	check.expect("parking_costs(False, 29)", parking_costs(False, 29), 508)
	## parked for 29 days, the first 4 weeks and 28 days, come out to
	## 120*7 = 480$
	## one extra day at 28$ is added, coming to a total of 508$
	

	check.expect("parking_costs(False, 34)", parking_costs(False, 34), 600)
	## parked for 34 days, the first 4 weeks and 28 days, come out to
	## 120*7 = 480$
	## 6 extra days round up to one additional week at 120$, coming to a
	## total of 600$


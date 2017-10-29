## Question 3
import check

locations = ["A", "B", "C", "D", "E", "F", "G"]

transportationAvailable = {"A":locations, \
							"B":["B", "D", "F", "G"],\
							"C":["C", "D", "G"],\
							"D":["D", "E", "G"],\
							"E":["E", "F", "G"],\
							"F":["F", "G"],\
							"G":["G"],\
							}

## takes a boolean and converts it to an equivalent string representation,
## True/False -> Yes/No

## boolToString: Bool -> Str

def boolToString(someBoolean):
	if(someBoolean == True):
		return "Yes"
	elif(someBoolean == False):
		return "No"
	else:
		return "Unknown"	


## returns whether or not a link is available from origin to destination

## linkAvailable: Str Str -> Bool

def linkAvailable(orig, dest):
	if(dest != orig):
		if(dest in transportationAvailable[orig]):
			return True
		else:
			return False
	else:
		return True
## checks if transportation is available from location orig to location dest,
## returns "Yes" if it is available, and "No" if not.

## direct_transportation: Str Str -> Str

def direct_transportation(orig, dest):
    return boolToString(linkAvailable(orig, dest))
    
if(__name__ == "__main__"):

	
	for origin in locations:
		print("\n", origin,)
		for destination in locations:
			print(destination, direct_transportation(origin, destination)),
			
	check.expect("direct_transportation('F', 'F')", direct_transportation('F', 'F'), "Yes")
	check.expect("direct_transportation('D', 'E')", direct_transportation('D', 'E'), "Yes")
	check.expect("direct_transportation('F', 'A')", direct_transportation('F', 'A'), "No")

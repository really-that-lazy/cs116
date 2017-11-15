## Question 1
import check

## Part a


## product takes a list of Natural numbers and returns the result of them
## multiplied together

## product: Listof(Nat) -> Nat

## someList must have 2 or more values      
      
 
## ie product([1,1,2,2,1,3]) => 12 
      
def product(someList):
	output = someList[0]
	for otherValues in someList[1:]:
		output *= otherValues
	return output
	
	
	
	
	
	
	
	
	
## calc_exp takes three natural numbers a, b, and n, and returns the following
## sum:
##
## b**1 + b**2 + ... + b**n + ((a+1)*(a+2)* ... (a+n))	
	
## calc_exp: Nat Nat Nat -> Nat

## ie calc_exp(2,2,2) => (2 + 2**2 + ((2+1)*(2+2)))
## => (2 + 4 + (3*4))
## => (6 + 12) => 18

def calc_exp(a,b,n):
	output = 0
	for i in range(1, n+1):
		output += (b**i)
	
	
	aPlusI = []
	for i in range(1, n+1):
		aPlusI += [a+i]
	
	##return output + product([(a+i) for i in range(1, n+1)])
	return output + product(aPlusI)	
	
if(__name__ == "__main__"):
	check.expect("calc_exp(10, 10, 1)", calc_exp(10, 10, 1), 21)
	check.expect("calc_exp(1, 3, 4)", calc_exp(1, 3, 4), 240)	
	check.expect("calc_exp(2, 2, 2)", calc_exp(2, 2, 2), 18)	


## filterButNotReallyFilter takes a list of values and applies a filter based on
## the predicate function filterCondition which is supplied as an argument. The
## function iterates across the list to be filtered and does not use recursion

## filterButNotReallyFilter: Listof(X) Function(X) -> Listof(X)

## where Function filterCondition must be a predicate

def filterButNotReallyFilter(someList, filterCondition):
	##output = [val for val in someList if (filterCondition(val) == True)]
	output = []
	for val in someList:
		if(filterCondition(val)):
			output += [val]
	return output


## isInt: X -> Bool

## return true if the value passed to the function is an int, false otherwise

def isInt(someValue):
	return (type(someValue) == int)

## isFloat: X -> Bool

## return true if the value passed to the function is a float, false otherwise

def isFloat(someValue):
	return (type(someValue) == float)

## isBool: X -> Bool

## return true if the value passed to the function is a boolean, false otherwise

def isBool(someValue):
	return (type(someValue) == bool)

## isStr: X -> Bool

## return true if the value passed to the function is a string, false otherwise

def isStr(someValue):
	return (type(someValue) == str)

## isAnythingElse: X -> Bool

## return true if the value passed to the function is anything but a string,
## boolean, float or int


def isAnythingElse(someValue):
	if( (not isFloat(someValue)) and (not isInt(someValue)) and (not isBool(someValue)) and (not isStr(someValue)) ):
		return True
	else:
		return False












## part b

## list_stat: Listof(Any) -> Listof(Int Int Int Int Int)

## produce a list with the number of Ints, floats, bools, strings, and other
## types of values found in the original list, in that order

def list_stat(lst):
	return [len(filterButNotReallyFilter(lst, isInt)), \
	 len(filterButNotReallyFilter(lst, isFloat)), \
	 len(filterButNotReallyFilter(lst, isBool)),\
	 len(filterButNotReallyFilter(lst, isStr)),\
	 len(filterButNotReallyFilter(lst, isAnythingElse))]


if(__name__ == "__main__"):
	check.expect("list_stat([3, 'wow', -3.967, True, True, False, 'nice'])", list_stat([3, 'wow', -3.967, True, True, False, 'nice']), [1,1,3,2,0])
	check.expect("list_stat(['good', [3,4], [10]])", list_stat(['good', [3,4], [10]]), [0,0,0,1,2])	








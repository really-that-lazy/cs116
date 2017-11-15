## Question 2
import check


## part a

## is odd takes a natural number and returns true if it is odd, false if
## otherwise

## isOdd: Nat -> Bool

## ie isOdd(3) => True
## isOdd(2) => False

def isOdd(someValue):
	if(someValue%2 == 0):
		return False
	else:
		return True

## create odds takes a natural number and returns an ascending list of all of
## the positive odd numbers less than or equal to it 

## create_odds: Nat -> Listof(Nat)

## ie create_odds(6) => [1,3,5]

def create_odds(target):
	if(target == 0):
		return []
	else:
		output = []
		for i in range(1, target+1):
			if(isOdd(i)):
				output += [i]
		##return [i for i in range(1, target+1) if isOdd(i)]
		return output



if(__name__ == "__main__"):
	check.expect("create_odds(8)", create_odds(8), [1,3,5,7])
	check.expect("create_odds(0)", create_odds(0), [])	
	check.expect("create_odds(1)", create_odds(1), [1])
	check.expect("create_odds(2)", create_odds(2), [1])








## part b

## build_special_list takes a natural number n, and builds a list of lists, the
## sublists containing a sequence of numbers from 1 to k, where k is a number
## between 1 and n which increases towards n with each sublist

## build_special_list: Nat -> Listof(Listof(Nat))

## ie build_special_list(3) => [[1],[1,2],[1,2,3]]

def build_special_list(n):
	containerList = []
	for i in range(1, n+1):
		subList = []
		for k in range(1, i+1):
			subList += [k]
		containerList += [subList]
    
    ##return [[k for k in range(1, i+1)] for i in range(1, n+1)]
	return containerList
    
    
if(__name__ == "__main__"):
	check.expect("build_special_list(6)", build_special_list(6), [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]])
	check.expect("build_special_list(0)", build_special_list(0), [])	    
	check.expect("build_special_list(1)", build_special_list(1), [[1]])









## part c

## isDivisible checks to see if n is divisible by value, true if it is, false
## otherwise

## isDivisible: Nat, Nat -> Bool

## ie isDivisible(3, 6) => True
## isDivisible(7, 22) => False

def isDivisible(value, n):	
	if((n%value) == 0):
		return True
	else:
		return False
		



## divisibles takes a natural number n, and returns a list of all of the numbers
## less than it that n is divisible by,

## divisibles: Nat -> Listof(Nat)

## ie divisibles(4) => [1,2]

def divisibles(n):
	listOfDivisibles = []
	for val in range(1, n):
		##print(val, n, isDivisible(val, n))
		if(isDivisible(val, n)):
			listOfDivisibles += [val]
				
		
	##return [val for val in range(1, n) if isDivisible(val, n)]
	return listOfDivisibles


if(__name__ == "__main__"):
	check.expect("divisibles(16)", divisibles(16), [1,2,4,8])
	check.expect("divisibles(0)", divisibles(0), [])	    
	check.expect("divisibles(1)", divisibles(1), [])
	check.expect("divisibles(19)", divisibles(19), [1])


	






## part d


## update_list takes a list of Integers and a pair of integers val and newval,
## replacing any occurences equal to val in the list with newval. The number of
## replacements made is returned at the end

## update_list: Listof(Int) Int Int -> Int

## ie update_list([1,0,0,1], 1, 2) => 2
## and the original list will be changed to [2,0,0,2]

def update_list(nlst, val, newval):
	changeCount = 0
	
	for i in range(0, len(nlst)):
		if(nlst[i] == val):
			nlst[i] = newval
			changeCount += 1 
	
	return changeCount
	
	
if(__name__ == "__main__"):

	nl = []

	check.expect("update_list(nl, 5, 10)", update_list(nl, 5, 10), 0)
	check.expect("nl", nl, [])	    
	
	newnl = [3, 10, 5, 10, -4]
	check.expect("update_list(newnl, 10, 7)", update_list(newnl, 10, 7), 2)
	check.expect("newnl", newnl, [3,7, 5, 7, -4])

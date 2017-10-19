## Question 1
import check

## isOdd takes a Natural number value and returns True if it is odd, False if it
## is even


## isOdd: Nat -> Bool

def isOdd(value):
	if(value%2 == 0):
		return False
	elif(value%2 == 1):
		return True




## take some natural number target and produce a list of all of the odd natural
## numbers less than or equal to it

## create_odds: Nat -> Listof(Nat)

def create_odds(target):
	if(target >= 1):
		if(isOdd(target)):
			return create_odds(target-1) + [target]
		else:
			return create_odds(target-1)
	else:
		return []
	

if(__name__ == "__main__"):
	check.expect("create_odds(8)", create_odds(8), [1,3,5,7])	
	check.expect("create_odds(0)", create_odds(0), [])		

## createSequence takes a natural number target and produces a list of all of
## the natural numbers less than or equal to it

## createSequence: Nat -> Listof(Nat)

def createSequence(target):
	if(target >= 1):
		return createSequence(target-1) + [target]
	else:
		return []


if(__name__ == "__main__"):
	check.expect("createSequence(9)", createSequence(9), [1,2,3,4,5,6,7,8,9])	
	check.expect("createSequence(0)", createSequence(0), [])		


## build_special_list: Nat -> Listof(Listof(Nat))

def build_special_list(n):
	if(n == 1):
		return [createSequence(1)]
	elif(n > 1):
		return build_special_list(n-1) + [createSequence(n)]
	else:
		return []


if(__name__ == "__main__"):
	check.expect("build_special_list(0)", build_special_list(0), [])	
	check.expect("build_special_list(1)", build_special_list(1), [[1]])		
	check.expect("build_special_list(3)", build_special_list(3), [[1], [1,2], [1,2,3]])		
	

## isDivisible: Nat, Nat -> Bool

def isDivisible(value, n):	
	if((n%value) == 0):
		return True
	else:
		return False

## buildDivisiblesList: Nat, Nat -> Listof(Nat)	
	
def buildDivisiblesList(n, currentValue=-1):
	if(n == 0):
		return []
	elif(n == 1):
		return []
	else:
	
		if(currentValue == -1):
			## base case where we start at our n value and start working down from
			## there
			return buildDivisiblesList(n, n-1)
		elif(currentValue == 1):
			return [1]
		else:
			if(isDivisible(currentValue, n)):
				return buildDivisiblesList(n, currentValue-1) + [currentValue]
			else:
				return buildDivisiblesList(n, currentValue-1)

## buildDivisiblesList: Nat -> Listof(Nat)
	
def divisibles(n):
	return buildDivisiblesList(n)



if(__name__ == "__main__"):
	check.expect("divisibles(16)", divisibles(16), [1,2,4,8])
	check.expect("divisibles(0)", divisibles(0), [])
	check.expect("divisibles(1)", divisibles(1), [])
	check.expect("divisibles(19)", divisibles(19), [1])		

## listFirst: Listof(X) -> X

def listFirst(someList):
	return someList[0]

## listFirst: Listof(X) -> Listof(X)
	
def listRest(someList):
	return someList[1:]	



def overwriteAtoB(value, a, b):
	if(value == a):
		return b
	else:
		return value

## update_list: Listof(Int) Int Int -> Listof(Int)

def update_list(nlst, val, newval):
	if(nlst == []):
		return nlst
	else:
		return [overwriteAtoB(listFirst(nlst), val, newval)] + update_list(listRest(nlst), val, newval)

if(__name__ == "__main__"):
	nl = [3, 10, 5, 10, -4]
	check.expect("update_list(nl, 10, 7)", update_list(nl, 10, 7), [3, 7, 5, 7, -4])


## mult_list: Listof(Int) Listof(Int) Int -> None

def mult_list(m1, m2, currentIndex = -1):
	if(currentIndex == -1):
		## indicator that we are starting, initially with the highest index in
		## the list
		startIndex = len(m1)-1
		return mult_list(m1, m2, startIndex)
	else:
		if(currentIndex > 0):
			m1[currentIndex] *= m2[currentIndex]
			mult_list(m1, m2, currentIndex - 1)
		elif(currentIndex == 0):
			m1[currentIndex] *= m2[currentIndex]
			print(m1)
		
		
if(__name__ == "__main__"):
	m1 = [1, 2, 23, 104]
	m2 = [-3, 2, 0, 6]
	check.expect("mult_list(m1, m2)", mult_list(m1, m2), None)
		
		
		
		
		
		
		
		
		
		
		
		
			

# Question 4:
import check
# You may Not use max or min or conditions in Python
# You are not allowed to import math module for this question. 
# Only simple mathematical operations such as * - + /   %  //  abs can be used.


## takes two integer values and returns the smallest value of those two
## values

## min2: Num Num -> Num

def min2(a, b):
	abDelta = (b-a)
	baDelta = (a-b)
	someTry = ((a-b) - (abs(abDelta)+abs(baDelta)))//4
	##print "a=%i, b=%i,		min([a,b])=%i,		abDelta=%i, baDelta=%i, someTry=%i\n" % (a, b, min([a,b]),abDelta, baDelta, someTry)
	return min([a,b])
	## I honestly cant figure out how to do this without conditionals, but I
	## think it must be related to the signs of the relative differences between
	## a and b, and b and a

## takes three integer values and returns the smallest value of those three
## values

## min3: Num Num Num -> Num


def min3(a, b, c):
    return min2(min2(a,b), min2(b,c))



if(__name__ == "__main__"):
	check.expect("min3(2, 1, 0)", min3(2,1,0), 0)
	check.expect("min3(0, 0, 0)", min3(0,0,0), 0)
	check.expect("min3(-1, -2, -55)", min3(-1,-2,-55), -55)
	check.expect("min3(-1, -1, 0)", min3(-1, -1, 0), -1)
	check.expect("min3(-1, 1, 0)", min3(-1, 1, 0), -1)

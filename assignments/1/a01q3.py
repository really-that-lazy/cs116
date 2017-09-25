# Question 3: 
import check

## takes a natural number n, and performs a series of operations on it, ending
## with the output being 15, regardless of the initial value of n

## forever_15: Nat -> Nat

def forever_15(n):
    output = n*3
    output += 45
    output *= 2
    output /= 6.0
    output -= n
    return output

if(__name__ == "__main__"):
	check.expect("forever_15(2)", forever_15(2), 15)
	check.expect("forever_15(4)", forever_15(4), 15)
	check.expect("forever_15(-1)", forever_15(-1), 15)
	check.expect("forever_15(0)", forever_15(0), 15)

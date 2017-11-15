## question 4
import check

## numberToDigits takes a natural number and converts it to a list of the digits
## that are used to represent it in a base 10 number system

## numberToDigits: Nat -> Listof(Nat)

## ie numberToDigits(68) => [6, 8]

def numberToDigits(someNumber):
	output = []
	
	while(someNumber >= 10):
		lastDigit = someNumber%10
		output = [int(lastDigit)] + output
		someNumber -= lastDigit
		someNumber /= 10
	output =  [int(someNumber)] + output
	return output

if(__name__ == "__main__"):	
	check.expect("numberToDigits(897)", numberToDigits(897), [8,9,7])
	check.expect("numberToDigits(197)", numberToDigits(197), [1,9,7])
	check.expect("numberToDigits(19)", numberToDigits(19), [1,9])	


## digit_sum takes a natural number and returns the digit sum, ie the sum of its
## digits in a base 10 number system repeated until the result is a single
## digit number

## digit_sum: Nat -> Nat

## ie digit_sum(123) => 6
## digit_sum(128) => 2

def digit_sum(num):
	while(num >= 10):
		num = sum(numberToDigits(num))
	return num

if(__name__ == "__main__"):
	
	check.expect("digit_sum(8)", digit_sum(8), 8)
	check.expect("digit_sum(897)", digit_sum(897), 6)
	check.expect("digit_sum(197)", digit_sum(197), 8)	
	check.expect("digit_sum(19)", digit_sum(19), 1)			

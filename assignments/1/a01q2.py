# Question 2:
import math
if(__name__ != "__main__"):
	import check

## helper function that calculates a piece of our normal distribution function,
## in this case the sigma*sqrt(2*pi)

## h1: Num, Num, Num -> Num

def h1(x, mean, std_dev):
	return (std_dev*(math.sqrt(2*math.pi)))

if(__name__ != "__main__"):
	check.within("h1", h1(1, 1, 2), 5.0132, 0.01)

## helper function that calculates a piece of our normal distribution function,
## in this case the sigma*sqrt(2*pi)

## h2: Num, Num, Num -> Num

def h2(x, mean, std_dev):
	return math.exp(((x-mean)**2)/(2*(std_dev**2)))
	
	
## returns the probability density of a normal distribution with parameters mean
## and std_dev at some point x. Output should be between 0 and 1 inclusive

## normal_distribution: Num, Num, Num -> Num
	
def normal_distribution(x, mean, std_dev):
	return (1.0/(h1(x, mean, std_dev)*h2(x, mean, std_dev)))
	
if(__name__ != "__main__"):
	check.within("normal_distribution", normal_distribution(3.0, 5.0, 2.0), 0.12098, 0.001)


if(__name__ == "__main__"):
	print(normal_distribution(3.0, 5.0, 2.0))
	print(h1(1,1,2))
	print(4*math.pi)

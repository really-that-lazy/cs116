## Question 3
import check

## most frequent takes a list of integers and returns a list containing the most
## frequent value, or multiple values if there is a tie, listed in the same
## order in which they first appeared in the list

## most_frequent: Listof(Int) -> Anyof(Listof(Int) Empty)

## most_frequent([1,3,3,0,2,2]) => [3,2]

def most_frequent(nlst):
	currentHighestCount = 0
	currentMostCommonValue = []
	
	for val in nlst:
		countOfThatVal = 0
		for cy in nlst:
			if(cy == val):
				countOfThatVal += 1
		countOfThatVal -= 1
		if(countOfThatVal > currentHighestCount):
			currentMostCommonValue = [val]
			currentHighestCount = countOfThatVal
		elif(countOfThatVal == currentHighestCount):
			if(val not in currentMostCommonValue):
				currentMostCommonValue += [val]
			currentHighestCount = countOfThatVal
	return currentMostCommonValue
	
	
	
if(__name__ == "__main__"):
	check.expect("most_frequent([16, 0, 15, 16, 15, -10, 7])", most_frequent([16, 0, 15, 16, 15, -10, 7]), [16, 15])	
	check.expect("most_frequent([16, 0, 15, 16, 15, -10, 7, 16])", most_frequent([16, 0, 15, 16, 15, -10, 7, 16]), [16])	
	check.expect("most_frequent([1,2,3,4])", most_frequent([1,2,3,4]), [1,2,3,4])	
	check.expect("most_frequent([4,3,2,1])", most_frequent([4,3,2,1]), [4,3,2,1])


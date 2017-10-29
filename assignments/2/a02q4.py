## Question 4
import check

## remainder takes two integers a & b, & returns the equivalent of a%b, the
## remainder of a/b

## remainder: Int Int -> Int

## ie remainder(5, 2) => 1

def remainder(a,b):
	if(a == b):
		return 0
	elif(a < b):
		return a
	else:
		return remainder(a-b, b)

    
if(__name__ == "__main__"):

	check.expect("remainder(3, 2)", remainder(3, 2), 1)
	check.expect("remainder(164, 10)", remainder(164, 10), 4)
	check.expect("remainder(1, 1)", remainder(1, 1), 0)

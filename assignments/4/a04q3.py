## Question 3
import check

## A keycode is a list of length 2, [d, n] where
##   d is an int from 0 - 9 representing a digit on a phone keypad and
##   n is an int[>0], representing the number of times the key has
##        been pressed. The value of n will be less than or equal to
##        the number of symbols associated with d on a phone.














## translateKeycodeToCharacterString takes a keycode and translates it to a
## single character string in the same way that a numeric keypad
## can be used in English speaking countries to type text.

## translateKeycodeToCharacterString: keycode -> Str

## the values of d & n in keycode must correspond to valid indexes d & n-1 in
## the 2d list responses defined below 

## ie
## translateKeycodeToCharacterString([1, 3]) => '?'

def translateKeycodeToCharacterString(someKeycode):
	responses = [[' '], ['.', ',', '?'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
	return responses[someKeycode[0]][someKeycode[1]-1]



if(__name__ == "__main__"):

	check.expect("translateKeycodeToCharacterString([9, 4])", translateKeycodeToCharacterString([9, 4]), 'z')
	check.expect("compose_msg([0, 1])", translateKeycodeToCharacterString([0, 1]), ' ')
	check.expect("compose_msg([1, 3])", translateKeycodeToCharacterString([1, 3]), '?')




## compose_msg takes a list of keycodes and translates each one into a
## corresponding single character string in the same way that a numeric keypad
## can be used in English speaking countries to type text. Once a list of
## single output characters has been formed, theyre all appended together and
## returned


## compose_msg: Listof(keycode) -> Str

def compose_msg(keypresses):
	outputCharacters = list(map(lambda someKeycode: translateKeycodeToCharacterString(someKeycode), keypresses))
	## ie keypresses = [[6, 3], [0, 1], [5, 2]] -> ['o', ' ', 'k']
	return "".join(outputCharacters)
	## stitch them all together as one big list and return them


if(__name__ == "__main__"):

	check.expect("compose_msg([[6, 3], [0, 1], [5, 2]])", compose_msg([[6, 3], [0, 1], [5, 2]]), 'o k')
	check.expect("compose_msg([[0, 1], [9, 2], [0, 1]])", compose_msg([[0, 1], [9, 2], [0, 1]]), ' x ')
	check.expect("compose_msg([])", compose_msg([]), '')

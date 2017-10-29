##question 1
import check


## stringToList takes a string and breaks it into a list of strings containing
## each individual character in the original string as its own string

## stringToList: Str -> Listof(Str)

def stringToList(someStr):
	return [ch for ch in someStr]

## listToString takes a list of strings and combines them into one string, in
## the same order as the original list they were found in

## listToString: Listof(Str) -> Str

def listToString(someList):
	output = ""
	for charStr in someList:
		output = output + charStr
	return output
	
	
if(__name__ == "__main__"):

	check.expect("stringToList('aaba')", stringToList('aaba'), ['a', 'a', 'b', 'a'])	
	check.expect("listToString(['a', 'a', 'b', 'a'])", listToString(['a', 'a', 'b', 'a']), 'aaba')	
	

## samechars takes a string s1, and another string s2, returning True if the
## characters of s2 are contained in order in s1 (though not necessarily
## consecutively), and False where otherwise
	
## samechars: Str Str -> Bool	
	
def samechars(s1, s2):
	if(s2 == ""):
		return True
	firstOfS2 = stringToList(s2)[0]
	if(firstOfS2 not in s1):
		return False
	else:
		if(len(stringToList(s2)) < 2):
			return True
		else:
			return samechars(s1[s1.index(firstOfS2):], listToString(stringToList(s2)[1:]) )


if(__name__ == "__main__"):

	check.expect("samechars('', '')", samechars('', ''), True)	
	check.expect("samechars('acdbba', 'ada')", samechars('acdbba', 'ada'), True)	
	check.expect("samechars('acdbba', 'abd')", samechars('acdbba', 'abd'), False)	
	check.expect("samechars('acdbb', 'ada')", samechars('acdbb', 'ada'), False)	

	check.expect("samechars('ad', 'ada')", samechars('ad', 'ada'), False)	
	check.expect("samechars('ada', 'ada')", samechars('ada', 'ada'), True)	
	check.expect("samechars('a', 'a')", samechars('a', 'a'), True)	
	check.expect("samechars('a', 'b')", samechars('a', 'b'), False)	
	

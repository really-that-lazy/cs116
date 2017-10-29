##question 3
import check


## looks at a string psswdInput and returns true if there is a numeric character
## in that string, false if otherwise

## passwordHasNumber: Str -> Bool

def passwordHasNumber(psswdInput):
	numeros = "0123456789"
	
	if(psswdInput == ""):
		return False
	elif(psswdInput[0] in numeros):
		return True
	else:
		return passwordHasNumber(psswdInput[1:])
	

if(__name__ == "__main__"):

	check.expect("passwordHasNumber('password')", passwordHasNumber('password'), False)
	## I can just hear the sysadmins twitching right now
	check.expect("passwordHasNumber('password123')", passwordHasNumber('password123'), True)




## looks at a string psswdInput and returns true if there is a lowercase letter
## character in that string, false if otherwise

## passwordHasLowercase: Str -> Bool

def passwordHasLowercase(psswdInput):
	loweros = "abcdefghijklmnopqrstuvwxyz"
	
	if(psswdInput == ""):
		return False
	elif(psswdInput[0] in loweros):
		return True
	else:
		return passwordHasLowercase(psswdInput[1:])

if(__name__ == "__main__"):

	check.expect("passwordHasLowercase('password')", passwordHasLowercase('password'), True)
	check.expect("passwordHasLowercase('PASSWORD123')", passwordHasLowercase('PASSWORD123'), False)


## looks at a string psswdInput and returns true if there is a uppercase letter
## character in that string, false if otherwise

## passwordHasUppercase: Str -> Bool

def passwordHasUppercase(psswdInput):
	upperos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	if(psswdInput == ""):
		return False
	elif(psswdInput[0] in upperos):
		return True
	else:
		return passwordHasUppercase(psswdInput[1:])
		
if(__name__ == "__main__"):

	check.expect("passwordHasUppercase('password')", passwordHasUppercase('password'), False)
	check.expect("passwordHasUppercase('PASSWORD123')", passwordHasUppercase('PASSWORD123'), True)


## checks if there is at least one numeric character, uppercase character, and
## lowercase character in a string psswdInput, and returns true if one of each
## is found, false otherwise

## passwordAcceptCheck: Str -> Bool

def passwordAcceptCheck(psswdInput):
	if((passwordHasNumber(psswdInput) and passwordHasLowercase(psswdInput)) and passwordHasUppercase(psswdInput)):
		return True
	else:
		return False



if(__name__ == "__main__"):

	check.expect("passwordAcceptCheck('password')", passwordAcceptCheck('password'), False)
	check.expect("passwordAcceptCheck('password123')", passwordAcceptCheck('password123'), False)
	check.expect("passwordAcceptCheck('PASSWORD123')", passwordAcceptCheck('PASSWORD123'), False)
	check.expect("passwordAcceptCheck('PASSWORD')", passwordAcceptCheck('PASSWORD'), False)
	check.expect("passwordAcceptCheck('paSSword')", passwordAcceptCheck('paSSword'), False)
	check.expect("passwordAcceptCheck('Passw0rd')", passwordAcceptCheck('Passw0rd'), True)
	## clearly the most secure option
	
	check.expect("passwordAcceptCheck('Password999?')", passwordAcceptCheck('Password999?'), True)

## return the number of special characters, ie any character defined in 
##	"!@#$%^&*()_+-=~,./<>?;':| "
## found in the string psswdInput 

## passwordSpecialCharacterCount: Str -> Nat

def passwordSpecialCharacterCount(psswdInput):
	
	specialCharacters = "!@#$%^&*()_+-=~,./<>?;':| "
	## apparently space is now a 'special character'
	
	if(psswdInput == ""):
		return 0
	elif(psswdInput[0] in specialCharacters):
		return 1 + passwordSpecialCharacterCount(psswdInput[1:])
	else:
		return passwordSpecialCharacterCount(psswdInput[1:])


## return the subjective 'score' or rating of a string psswdInputs password
## 'strength' as defined by the rules defined in A03.pdf

## passwordNumericScore: Str -> Num

def passwordNumericScore(psswdInput):
	score = 0
	if(len(psswdInput) < 5):
		score -= 10
	elif(len(psswdInput) > 8):
		score += 15
	
	specialCount = passwordSpecialCharacterCount(psswdInput)
	if(specialCount > 2):
		score += ((specialCount-1)*10)
	return score


## categorizes a number as either "weak", "medium", or "strong" based on the
## criteria defined in A03.pdf

## passwordScoreCategory: Num -> Str	
	
def passwordScoreCategory(passwordScore):
	if(passwordScore < 25):
		return "weak"
	elif(passwordScore <= 40):
		return "medium"
	else:
		return "strong"	

if(__name__ == "__main__"):

	check.expect("passwordScoreCategory(0)", passwordScoreCategory(0), "weak")
	check.expect("passwordScoreCategory(25)", passwordScoreCategory(25), "medium")
	check.expect("passwordScoreCategory(39)", passwordScoreCategory(39), "medium")
	check.expect("passwordScoreCategory(40)", passwordScoreCategory(40), "medium")
	check.expect("passwordScoreCategory(50)", passwordScoreCategory(50), "strong")

## takes a string password and checks to see if it meets basic criteria for a
## password, returning a string with its numeric strength and the category that
## strength fall into, or False if it fails, printing a failure message msg1 to
## the console	
	
## password_check: Str -> Anyof(Bool Str)	
			
def password_check(password):
	
	msg1 = 'The password ("{0}") failed a basic test'
	res1 = "strong"
	res2 = "medium"
	res3 = "weak"
   
	if(passwordAcceptCheck(password) == True):
		return "%i:%s" % (passwordNumericScore(password), passwordScoreCategory(passwordNumericScore(password)) )
	else:
		print(msg1.format(password))
		return False


if(__name__ == "__main__"):

	check.expect("password_check('Xy 37 1-0')", password_check('Xy 37 1-0'), "35:medium")
	check.expect("password_check('Password999?')", password_check('Password999?'), "15:weak")

	check.expect("password_check('Yt3)(*&a%')", password_check('Yt3)(*&a%'), "55:strong")

	check.expect("password_check('PaSsWoRd')", password_check('PaSsWoRd'), False)
	check.expect("password_check('hello12')", password_check('hello12'), False)

##question 2
import check

## asks the user for input in the console, returning None if the input is equal
## to the noneFlag string (easy way to detect the user not wanting to answer
## at this time), and the prompt string is printed to console on each request
## for input

## promptUserInput: Str Str -> Str

def promptUserInput(prompt, noneFlag):
	output = input(prompt+" ")
	if(output == noneFlag):
		return None
	elif(output == ""):
		return promptUserInput(prompt, noneFlag)
	else:
		return output

## takes a first, last name, and year as strings, and formats it according to
## the rules defined in A03.pdf

## formatInputsAsUsername: Str Str Str -> Str

def formatInputsAsUsername(fNameInput, lNameInput, bYearInput):
	return str.lower(fNameInput[0]) + str.lower(lNameInput[-4:]) + bYearInput[2] + bYearInput[1] + bYearInput[0]

if(__name__ == "__main__"):

	check.expect("formatInputsAsUsername('Mike', 'Brown', '1989')", formatInputsAsUsername('Mike', 'Brown', '1989'), 'mrown891')
	check.expect("formatInputsAsUsername('Young', 'Hu', '1991')", formatInputsAsUsername('Young', 'Hu', '1991'), 'yhu991')
	check.expect("formatInputsAsUsername('Y', 'U', '1202')", formatInputsAsUsername('Y', 'U', '1202'), 'yu021')
	check.expect("formatInputsAsUsername('hodor', '', '1111')", formatInputsAsUsername('hodor', '', '1111'), 'h111')

## generate_username prompts the user for 3 strings, namely the first name,
## last name, and birth year of the user, then returns it formatted as a
## username using the formatInputsAsUsername function defined above

## generate_username: None -> Str

def generate_username():
    inp1 = 'Enter your first name:'
    inp2 = 'Enter your last name:'
    inp3 = 'Enter your birth year:'
    return formatInputsAsUsername(promptUserInput(inp1, "None"), promptUserInput(inp2, "None"), promptUserInput(inp3, "None"))


if(__name__ == "__main__"):
	print(generate_username())


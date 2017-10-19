## Question 2
import check

## A tweet is a String of any length, where the following requirements are met:
##   the start of the string is the character '#'
##   an integer tweetNumber is stored after the '#' character, but before the
##        first occurrence of ':-' in the string
##   a string tweetAuthor is stored beginning with the '@' character after the
##        first occurrence of ':-', and before the second occurrence of ':-'
##   a string tweetContent is stored after the second occurrence of ':-'


## tweet constants for tests
tweet1 = "#1:-@DanClark:-The party was amazing" 
tweet19 = "#19:-@NatalyS:-Avoid 401 Toronto area at this time" 
tweet50 = "#50:-@CBCNews:-How Canadian captain gave her team a speech" 
tweet14 = "#14:-@DanClark:-The food was good"
tweet15 = "#15:-@DaveLin:-Lucky you DanClark"
tweets =   [tweet1, tweet19, tweet50, tweet14, tweet15]





## return the tweetNumber of a given tweet

## getTweetNumber: tweet -> Int

## ie
## getTweetNumber(tweet1) => 1

def getTweetNumber(tweet):
	firstSeparatorIndex = tweet.find(":-")
	return int(tweet[1:firstSeparatorIndex])

if(__name__ == "__main__"):

	check.expect("getTweetNumber(tweet1)", getTweetNumber(tweet1), 1)
	check.expect("getTweetNumber(tweet19)", getTweetNumber(tweet19), 19)
	check.expect("getTweetNumber(tweet50)", getTweetNumber(tweet50), 50)







## return the tweetAuthor of a given tweet

## getTweetAuthor: tweet -> Str

## ie
## getTweetNumber(tweet1) => 'DanClark'

def getTweetAuthor(tweet):
	firstSeparatorIndex = tweet.find(":-")	
	secondSeparatorIndex = tweet.find(":-", firstSeparatorIndex+2)
	authorString = tweet[firstSeparatorIndex+2:secondSeparatorIndex]	
	return authorString[1:]
	## chop off the '@' symbol at the start of the name

if(__name__ == "__main__"):

	check.expect("getTweetAuthor(tweet1)", getTweetAuthor(tweet1), 'DanClark')
	check.expect("getTweetAuthor(tweet19)", getTweetAuthor(tweet19), 'NatalyS')
	check.expect("getTweetAuthor(tweet50)", getTweetAuthor(tweet50), 'CBCNews')






## tweetIsByAuthor returns True if a tweet has the same tweetAuthor as author,
## False if otherwise

## tweetIsByAuthor: tweet Str -> Bool

def tweetIsByAuthor(tweet, author):
	if(getTweetAuthor(tweet) == author):
		return True
	else:
		return False


if(__name__ == "__main__"):

	check.expect("tweetIsByAuthor(tweet1, 'DanClark')", tweetIsByAuthor(tweet1, 'DanClark'), True)
	check.expect("tweetIsByAuthor(tweet1, 'NatalyS')", tweetIsByAuthor(tweet1, 'NatalyS'), False)
	check.expect("tweetIsByAuthor(tweet1, '')", tweetIsByAuthor(tweet1, ''), False)


## search_tweets takes a list of tweets, filters them based on whether their
## tweetAuthor matches the input string tweeter, then returns a list of the
## tweet numbers of those that were filtered

## search_tweets: Listof(tweet) Str -> Listof(Int)
		
def search_tweets(tweets, tweeter):
	matchedTweetList = list(filter(lambda tweet: tweetIsByAuthor(tweet, tweeter), tweets))
	if(matchedTweetList != []):
		return list(map(lambda tweet: getTweetNumber(tweet), matchedTweetList))
	else:
		return matchedTweetList

if(__name__ == "__main__"):

	check.expect("search_tweets(tweets, 'DanClark')", search_tweets(tweets, 'DanClark'), [1,14])
	check.expect("search_tweets(tweets, 'CBCNews')", search_tweets(tweets, 'CBCNews'), [50])
	check.expect("search_tweets(tweets, 'NatalyS')", search_tweets(tweets, 'NatalyS'), [19])

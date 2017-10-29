##question 4  
import check

## draw: Str Nat -> None

def draw(s,b):
	if(b == 0):
		print(s)
	if((b > 1)or(b < 0)):
		sLen = len(s)
		newS = s*abs(b)
		
		
		if(b > 1):
			##print(sLen, b, sLen/b)
			draw(newS[-(b*):], 0)
			draw(newS, b-1)
	elif(b == 1):
		##draw(s, 0)
		print(repr(s))
		print("="*10)
		
	##draw(s,-b)
		

def drawBak(s,b):
	if(b == 0):
		print(s)
	elif((b > 1)or(b < 0)):
		
		if(b > 1):
			draw(s*abs(b), 0)
		elif(b < 0):
			draw(s, 0)
					
		if(b > 1):
			draw(s, b-1)
		elif(b < 0):
			draw(s+s[0], b+1)				
	elif(b == 1):
		draw(s, 0)
		print("="*10)
	##draw(s,-b)
		



if(__name__ == "__main__"):
	draw("*", 6)
	draw("(*)", 6)
	##draw("*", -6)
    
def draw_diamond(rows):
	pass
    

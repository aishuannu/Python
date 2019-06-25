def findIntegers(s):
	'''
	0  ---> outside and not ready to enter
	1  ---> outside but ready to enter
	2  ---> inside
	'''
	state = 1
	ans = []
	i = 0
	nextint = []
	e = len(s)
	while (i < e):
		if state == 0 :
			if  (not s[i].isdigit()) and (not (s[i] == ".")):
				state = 1
		elif (state == 1):
			if s[i].isdigit():
				state = 2
				nextint = [s[i]]
			elif s[i] == ".":
				state = 0
		elif (state == 2):
			if s[i].isdigit():
				nextint.append(s[i])
			elif (s[i] == ".") and (i < e-1) and (s[i+1].isdigit()):
				state = 0
			else:
				ans.append("".join(nextint))
				state = 1
		i = i+1
	return(ans)

ls = '''
This is a long sentence, of more than 20 letters and 8 words. I may have
real numbers such as 3.14 in this, but it should not print them out. But
integers can be the last word in a sentence such as 30. The word a39b contains
the integer 39..45 and .382. Does it work with .45?
'''

print(findIntegers(ls))
				

				

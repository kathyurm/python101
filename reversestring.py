# given a string, return a new string w/ the reversed order of characters 
#! /usr/bin/env/python3

def reverse(s):
	newstr=[]
	for i in range(len(s),0,-1):
		if s[i-1] != []:
			newstr.append(s[i-1])
		print (i)
	print str(newstr)

print ('Give me a word to reverse.') 
st = input()
#st = 'hello'
reverse(st)

#write a program that console logs the numbers from 1 to n. 
#for multiples of three, print fizz
#for multiples of five, print buzz
#for numbers which are multiples of both three and five print "fizzbuzz"


def fizzBuzz(n):
	for i in range(1, n+1):
		if (i % 3==0) and (i %5==0):
			print (str(i) + ': fizzbuzz!')
		elif i % 5 == 0: 
			print (str(i) + ': buzz')
		elif i % 3==0:
			print (str(i) + ': fizz')
		else:
			print (str(i))
	print ("\n")


print ('Please enter a number to FizzBuzz')
usernum = input()

fizzBuzz(usernum)

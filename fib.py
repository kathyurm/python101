# print out the nth entry in the fibonacci series
# 0,1,1,2,3,5,8,13,21,34


def fib(nth):
	if nth<2: #the 0th = 0, the 1st=1
	  return nth
	else: 
	  return fib(nth-1) + fib(nth-2) #the 2nd = fib(1) + fib (2); 

print ('Enter how many entries of the Fibonacci series you would like to see')
n = input()
print ('the ' + str(n) + 'th element in the fibonacci sequence is ' + str(fib(n)))



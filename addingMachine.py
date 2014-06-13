def add_two (*args):
  num1, num2 = args
  sum = int(num1) + int(num2)
  print sum

def sub_two (*args):
  num1, num2 = args
  sub = int(num1) - int(num2)
  print sub

def mult_two (*args):
  num1, num2 = args
  product = int(num1) * int(num2)
  print product

def div_two (*args):
  num1, num2 = args
  div = int(num1) / int(num2)
  print div

input1 = raw_input("num1?")
input2 = raw_input("num2?")
operand = raw_input("choose one: +, -, *, /: ")

if operand == "+":
 add_two(input1, input2)
elif operand == "-":
  sub_two(input1, input2)
elif operand == "*":
  mult_two(input1, input2)
elif operand == "/":
  div_two(input1, input2) 
else:
  print ("invalid operand. aborting program...")



#add
def add(a,b):
  return a+b
#subtract
def subtract(a,b):
  return a-b
#multiply
def multiply(a,b):
  return a*b
#divide
def divide(a,b):
  return a/b

operations = {
"+":add, 
"-":subtract, 
"*":multiply, 
"/":divide
}

num1 = int(input("What is the first number? "))

for i in operations:
  print(i)
operator = input("Pick an operator from above: ")
answer = operations[operator]
num2 = int(input("What is the second number? "))
print(f"{num1} {operator} {num2} = {answer(num1, num2)}")
first_answer = answer(num1, num2)

continue1 = input("Type 'y' to continue or 'n' to exit ")
second_answer = first_answer
while continue1 == 'y':
  
  new_answer = float(second_answer)
  operator = input("Pick another operator: ")
  num3 = int(input("Next number?: "))
  answer1 = operations[operator]
  second_answer = answer1(new_answer, num3)
  print(f"{new_answer} {operator} {num3} = {second_answer}")
  continue1 = input("Type 'y' to continue or 'n' to exit ")
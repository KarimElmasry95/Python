#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
l_passward = ''
s_passward = ''
n_passward = ''
ordered_passward = ''
passward = ''
y = ''
for i in range(nr_letters):
  l_passward += random.choice(letters)
for i in range(nr_symbols):
  s_passward += random.choice(symbols)
for i in range(nr_numbers):
  n_passward += random.choice(numbers)
ordered_passward = l_passward + s_passward + n_passward
print(ordered_passward)

for i in range(len(ordered_passward)):
  x = random.choice(ordered_passward)
  passward += x
  if ordered_passward.count(x) == 1:
    ordered_passward = ordered_passward.replace(x,"")
   
  elif ordered_passward.count(x) > 1:
    ordered_passward = ordered_passward.replace(x,"") + ((ordered_passward.count(x) - 1)*x)
    
  
print(passward)
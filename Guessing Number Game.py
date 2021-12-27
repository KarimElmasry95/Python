#Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
difficulty = (str(input("Choose a difficulty. Type 'easy' or 'hard': "))).lower()


number = random.randint(1,100)  
flag = False
while flag == False:
    if difficulty == 'easy':
        attempts = 10
        flag = True
        print(f"You have {attempts} attempts remaining to guess the number")
    elif difficulty == 'hard':
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number")
        flag = True
    else:
        print("Invalid")
        difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))

  
  

guess = int(input("Make a guess: "))
for i in range(attempts):
  if guess > number:
    attempts -= 1
    if attempts == 0:
      print("Too High")
      print(f"You have {attempts} attempts remaining to guess the number")
      print(f"You have run out of guesses, you lose")
    else:
      print("Too High")
      print("Guess again")
      print(f"You have {attempts} attempts remaining to guess the number")
      guess = int(input("Make a guess: "))
  elif guess < number:
    attempts -= 1
    if attempts == 0:
      print("Too Low")
      print(f"You have {attempts} attempts remaining to guess the number")
      print(f"You have run out of guesses, you lose")
    else:
      print("Too Low")
      print("Guess again")
      print(f"You have {attempts} attempts remaining to guess the number")
      guess = int(input("Make a guess: "))
    
  elif guess == number:
    print(f"You got it! The answer was {number}")
    break

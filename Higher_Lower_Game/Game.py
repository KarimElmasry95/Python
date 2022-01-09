import art
import game_data
import random
import replit
print(art.logo)
score = 0
winner = " "
Flag_A = random.choice(game_data.data)
Flag_B = random.choice(game_data.data)
game_over = False
#print(Flag_A)
#print(Flag_B)


def winners():
  global winner
  if Flag_A['follower_count'] > Flag_B['follower_count']:
    winner = "a"
  else:
    winner = "b"  
  print(winner)

def compare():
  print(f"Compare A: {Flag_A['name']}, a {Flag_A['description']}, from {Flag_A['country']}")
  print(art.vs)
  print(f"Compare B: {Flag_B['name']}, a {Flag_B['description']}, from {Flag_B['country']}")
  
def invalid():
  global guess
  while guess != 'a' and guess != 'b':
    print("Invalid Input! Try again.")
    guess = input("Who has more followers? Type A or B ").lower()

compare()
winners()
guess = input("Who has more followers? Type A or B ").lower()
invalid()

while game_over == False:
  if guess == winner and winner == 'b':
    score += 1
    Flag_A = Flag_B
    Flag_B = random.choice(game_data.data)
    replit.clear()
    print(f"You are right. Current score: {score}")
    compare()
    winners()
    guess = input("Who has more followers? Type A or B ").lower()
    invalid()
  elif guess == winner and winner == 'a':
    score += 1
    Flag_B = random.choice(game_data.data)
    replit.clear()
    print(f"You are right. Current score: {score}")
    compare()
    winners()
    guess = input("Who has more followers? Type A or B ").lower()
    invalid()
  else:
    replit.clear()
    print(f"Game Over!  Final score: {score}")
    game_over = True



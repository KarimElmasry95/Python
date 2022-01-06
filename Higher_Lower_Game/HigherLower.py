import art
import game_data
import random
print(art.logo)
score = 0
Flag_A = random.choice(game_data.data)
Flag_B = random.choice(game_data.data)
game_over = False
print(Flag_A)
print(Flag_B)
print(" \n")
def compare():
  
  print(f"Compare A: {Flag_A['name']}, a {Flag_A['description']}, from {Flag_A['country']}")
  print(art.vs)
  print(f"Compare B: {Flag_B['name']}, a {Flag_B['description']}, from {Flag_B['country']}")
  winner = ""
  if Flag_A['follower_count'] > Flag_B['follower_count']:
    winner = "A"
  else:
    winner = "B"
compare()
guess = input("Who has more followers? Type A or B ").upper()

winner = ""
if Flag_A['follower_count'] > Flag_B['follower_count']:
    winner = "A"
else:
    winner = "B"  
  #print(winner)

while game_over == False:
  if guess == winner and winner == 'B':
    score += 1
    Flag_A = Flag_B
    Flag_B = random.choice(game_data.data)
    print(Flag_A)
    print(Flag_B)
    print(" \n")
    print(f"You are right. Current score: {score}")
    compare()
    guess = input("Who has more followers? Type A or B ")
  elif guess == winner and winner == 'A':
    score += 1
    Flag_B = random.choice(game_data.data)
    print(Flag_A)
    print(Flag_B)
    print(" \n")
    print(f"You are right. Current score: {score}")
    compare()
    guess = input("Who has more followers? Type A or B ")  
  else:
    print(f"Game Over!  Final score: {score}")
    game_over = True



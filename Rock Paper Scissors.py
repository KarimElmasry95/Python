rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
play = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
player_play = int(play)
comp_play = random.randint(0,2)

if player_play == 0:
  print("Player plays Rock")
  print(rock)
  
elif player_play == 1:
  print("Player plays Paper")
  print(paper)
elif player_play == 2:
  print("Player plays Scissors")
  print(scissors)

if comp_play == 0:
  print("Computer plays Rock")
  print(rock)
  
elif comp_play == 1:
  print("Computer plays Paper")
  print(paper)
elif comp_play == 2:
  print("Computer plays Scissors")
  print(scissors)

if player_play > 2 or player_play < 0:
  print("Invalid Input. Player Loses!")
elif comp_play == player_play:
  print("Draw")
elif comp_play == 2 and player_play == 0:
  print("Player Wins!")
elif player_play == 2 and comp_play == 0:
  print("Computer Wins!")
elif player_play > comp_play:
  print("Player Wins!")
elif comp_play > player_play:
  print("Computer Wins!")


import replit
import art
from operator import itemgetter
print(art.logo)
more_bids = 'yes'
bid_info = {}
while more_bids == 'yes':
  
  name = input("What is your name?: ")
  bid = int(input("What is your bid? $"))
  more_bids = input("Are there any other bidders? Type 'yes' or no ")
  if more_bids == 'yes':
    replit.clear()
  bid_info[name] = bid

winner = ""
highest_bid = 0
for i in bid_info:
  if bid_info[i] > highest_bid:
    highest_bid = bid_info[i]
    winner = i

print("The winner is " + str(winner) + " with a bid of $" + str(highest_bid))
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

sorted1 = dict(sorted(bid_info.items(), key=itemgetter(1)))
winner = list(sorted1.keys())
highest_bid = list(sorted1.values())
x = winner[-1]
y = highest_bid[-1]

print("The winner is " + str(x) + " with a bid of $" + str(y) )
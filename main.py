'''
Johnny Olmedo
- This program is a silent auction program that allows users to enter for a bid, then decides who has the highest bid
- The focus of this programming exercise to to work with dictionaries and nesting
'''

import os
from art import logo
# display logo
print(logo)
# create empty dictionary for bids
bids = {}
bidding_finished = False # set to false to force the 'while not bidding_finished' call

# this function decides whos the highest bidder
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    # the bid amount should equal the value pair of said key
    bid_amount = bidding_record[bidder]
    # decide whether the bid is the highest or not
    if bid_amount > highest_bid: 
      # set new highest bid
      highest_bid = bid_amount
      # declare new winner
      winner = bidder # notice winner = bidder (ith iterator variable), this will give us the name
  print(f"The winner is {winner} with a bid of ${highest_bid}")

# while bidding_finished = True
while not bidding_finished:
  # grab the user info 
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  # set bid in bid dictionary
  bids[name] = price
  # does user want to continue
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  # if not find the highest bid
  if should_continue == "no":
    bidding_finished = True # set to true
    find_highest_bidder(bids)
  # if they do want to continuue
  elif should_continue == "yes":
      # clear cosole
    os.system('clear')
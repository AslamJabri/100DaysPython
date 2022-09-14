import os
from art import logo

print(logo)
print("Welcome to the secret auction program")

bids = {}

bidding_finished = False

def winner(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $ ")) 
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no .'")

    if should_continue == "no":
        bidding_finished = True
        winner(bids)
    elif should_continue == "yes":
        os.system('clear')
    

        

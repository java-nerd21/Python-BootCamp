#from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program.")
bidders_left = "yes"
auction_name_bids = {}
while bidders_left == "yes":
    name = input("What is your name?: ")
    bid = input("What's your bid?: €")
    auction_name_bids[name] = bid
    bidders_left = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    #clear()



print(auction_name_bids)

highest_bid = max(auction_name_bids, key=auction_name_bids.get)

print(
    f"The winner is {highest_bid} with a bid of €{auction_name_bids[highest_bid]}"
)

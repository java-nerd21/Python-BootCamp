from art import logo
from art import vs
from game_data import data
import random

def random_account():
    """Get a random account"""
    return random.choice(data)

def format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description}, from {country}."

def compare_accounts(account_a, account_b):
    """Compare two accounts followers"""
    if account_a["follower_count"] > account_b["follower_count"]:
        return "A"
    else:
        return "B"



def play_game():
    print(logo)
    
    is_game_over = False
    account_a = random_account()
    account_b = account_a
    score = 0
    
    while not is_game_over:
        while account_a == account_b:
            account_b = random_account()

        print("Compare A: " + format(account_a))
        print(vs)
        print("Compare B: " + format(account_b))

        """Returns which player has more followers"""
        answer = compare_accounts(account_a, account_b)

        user_answer = input("Who has more followers? Type 'A' or 'B': ")

        if user_answer == answer:
            score += 1
            print(logo)
            print("You are correct! Current score is " + str(count))
        else:
            print("You are incorrect! Final score is " + str(count))
            is_game_over = True

        account_a = account_b
        

play_game()







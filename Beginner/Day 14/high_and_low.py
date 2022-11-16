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


account_a = random_account()
account_b = random_account()
print("Compare A: " + format(account_a))



# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

# 🚨 Don't change the code below 👇
from re import T


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name12 = name1.lower() + name2.lower()

T = int(name12.count("t"))
R = int(name12.count("r"))
U = int(name12.count("u"))
E = int(name12.count("e"))
L = int(name12.count("l"))
O = int(name12.count("o"))
V = int(name12.count("v"))
E = int(name12.count("e"))

true1 = T+R+U+E
love = L+O+V+E
true_love = true1*10 + love

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")
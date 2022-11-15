#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
import random

#Write the rest of your code below this line 👇
random_int = random.randint(1,2)

if random_int == 1:
    print("Heads")
else:
    print("Tails")
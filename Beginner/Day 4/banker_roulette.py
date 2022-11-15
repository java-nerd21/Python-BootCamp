# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

random_pick = random.randint(0, len(names)-1)
person_who_pays = names[random_pick]
print(person_who_pays + " is going to buy the meal today!")

# Or you can use choice() 

person_who_pays = random.choice(names)
print(person_who_pays + " is going to buy the meal today!")

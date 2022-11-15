#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)
days_left = years_left*365
weeks_left = years_left*52
months_left = years_left*12

#f-strings allow use of different types in one string using the below example
message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)
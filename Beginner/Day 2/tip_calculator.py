#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n€"))
tip = 1 + float(input("What percentage tip would you like to give? 10, 12, 15?\n")) / 100
people = int(input("How many people to split th bill?\n"))
bill_per_person = (bill / people) * tip

#Converts float to string and round it to two deicmal place
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: €{final_amount}")
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# ** put it to the power of the number flowing them
bmi_float = float(weight)/(float(height) ** 2)
int_bmi = int(bmi_float)
print(int_bmi)


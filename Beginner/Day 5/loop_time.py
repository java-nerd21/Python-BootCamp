fruits = ["Apple", "Peach","Pear"]
for fruit in fruits:
    print(fruit)


#loops with range function
for number in range(1, 10 , 3):
    #prints all number except 10 in range above, to include 10 must adjust range to 11
    print(number)

total =0
for number in range (1, 101):
    total += number
print(total)
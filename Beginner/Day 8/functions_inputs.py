# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet(name):
#     print(f"Hey {name}")
#     print(f"What's up, {name}?")
#     print(f"Nice weather, isn't it {name}")

# greet("Josh")

#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}\nWhat is it like in {location}?")
    
greet_with("Jame Wood","France")

greet_with("France", "James Wood")

greet_with(location="France", name="James Wood")
""" from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.forward(100)

my_screen = Screen()

"""

from prettytable import PrettyTable

table = PrettyTable() 
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)

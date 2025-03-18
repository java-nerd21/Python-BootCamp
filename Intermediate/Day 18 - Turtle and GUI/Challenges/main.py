from turtle import Turtle, Screen
import random

#timmy = Turtle()
#timmy.shape("turtle")
#timmy.color("red")

#Challenge 1 draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

#Challenge 2 draw a dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# #Challenge 3 - Drawing Different Shapes
#colors = ["red", "blue", "green", "black", "purple", "orange"]

# for i in range(3, 11): #number of sides
#     timmy.color(colors[i-3]) #color of the shape

#     for _ in range(i):
#         timmy.forward(100) #length of each side
#         timmy.right(360/i) #angle = 360/number of sides

# #Day 18 Challenge 4 - Random Walk
# timmy.pensize(15)
# timmy.speed("fastest")

# directions = [0, 90, 180, 270]

# for _ in range(100):
#     timmy.color((random.random(), random.random(), random.random()))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# # #Day 18 Challenge 5 - Change colour using RGB function
# def random_color():
#     r = random.randint(0, 255) / 255.0
#     g = random.randint(0, 255) / 255.0
#     b = random.randint(0, 255) / 255.0
#     random_color = (r, g, b)
#     return (random_color)

# timmy.pensize(15)
# timmy.speed("fastest")

# directions = [0, 90, 180, 270]

# for _ in range(100):
#      timmy.color(random_color())
#      timmy.forward(30)
#      timmy.setheading(random.choice(directions))

# #Day 18 Challenge 6 - Spirograph
# timmy.speed("fastest")
# timmy.pensize(2)
# timmy.hideturtle()

# for i in range(0, 360, 5): #angle
#     timmy.color(random_color())
#     timmy.setheading(i)
#     timmy.circle(100)












Screen = Screen()
Screen.exitonclick()
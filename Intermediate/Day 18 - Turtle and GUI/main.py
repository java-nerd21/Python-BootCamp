from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

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

#Challenge 3 - Drawing Different Shapes
colors = ["red", "blue", "green", "black", "purple", "orange"]

for i in range(3, 11): #number of sides
    timmy.color(colors[i-3]) #color of the shape

    for _ in range(i):
        timmy.forward(100) #length of each side
        timmy.right(360/i) #angle = 360/number of sides


















Screen = Screen()
Screen.exitonclick()
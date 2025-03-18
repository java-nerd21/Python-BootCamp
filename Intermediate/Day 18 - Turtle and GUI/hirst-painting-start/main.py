###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import os

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, 'image.jpg')

rgb_colors = []
colors = colorgram.extract(image_path, 30)
#colors = colorgram.extract(r'C:\Users\Joshua\OneDrive\Documents\GitHub\Python-BootCamp\Intermediate\Day 18 - Turtle and GUI\hirst-painting-start\image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(rgb_colors)

colour_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
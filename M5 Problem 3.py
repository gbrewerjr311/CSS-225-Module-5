#Greg Brewer
#May 14, 2023
# Pologyn

import turtle

# Prompt the user for the number of sides, length of the side, line color, and fill color
num_sides = int(input("Enter the number of sides: "))
side_length = int(input("Enter the length of each side: "))
line_color = input("Enter the color of the lines: ")
fill_color = input("Enter the fill color: ")

# Create a turtle object and set its attributes
t = turtle.Turtle()
t.pencolor(line_color)
t.fillcolor(fill_color)

# Calculate the angle for each side of the polygon
angle = 360 / num_sides

# Move the turtle to the starting position
t.penup()
t.goto(-side_length/2, 0)
t.pendown()

# Draw the polygon and fill it in
t.begin_fill()
for i in range(num_sides):
    t.forward(side_length)
    t.right(angle)
t.end_fill()

# Keep the turtle window open until the user closes it
turtle.done()

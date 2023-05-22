#Greg Brewer
#May 14, 2023
# Pictures



import turtle

# Set up the turtle object
t = turtle.Turtle()
t.speed("fastest")
t.pensize(3)

# Draw the stem
t.penup()
t.goto(0, -200)
t.pendown()
t.color("green")
t.goto(0, -50)

# Draw the flower petals
for i in range(12):
    t.color("yellow")
    t.begin_fill()
    t.circle(50, 90)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.circle(50, 90)
    t.end_fill()
    t.right(30)

# Draw the center of the flower
t.color("brown")
t.penup()
t.goto(0, 0)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

# Hide the turtle cursor and keep the window open
turtle.done()

import turtle

# Create a new turtle object
wn = turtle.Screen()
wn.bgcolor("lightgreen")

t = turtle.Turtle()
t.color("red")
t.pensize(3)

# Move the turtle
t.forward(50)
t.left(90)
t.forward(50)

# Write something on the screen
t.penup()
t.goto(-100, 50)
t.write("Hello, Turtle!", align="center", font=("Arial", 24, "normal"))

wn.mainloop()  # This keeps the turtle window open

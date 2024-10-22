import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightblue")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

lenghtsquare = figures.draw_square('insert the lenght: ')
lenghttriangle = figures.draw_square('insert the lenght: ')
lenghta = figures.draw_square('insert the lenght: ')
lenghtb = figures.draw_square('insert the lenght: ')
# Draw a square
for i in range(4):
    pen.forward(lenghtsquare)
    pen.right(90)

#draw a triangle
for i in range(3):
    pen.forward(lenghttriangle)
    pen.right(120)

#draw a rectangle
for i in range(2):
    pen.forward(lenghta)
    pen.right(90)
    pen.forward(lenghtb)
    pen.right(90)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()


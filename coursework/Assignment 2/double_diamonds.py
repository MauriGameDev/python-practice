"""this program is to generate two diamonds using turtle graphics"""

import turtle

# predefine the diamond side length
SIDE_LENGTH = 150

# predefine the fill color
COLOR = 'blue'

# setup the turtle window
turtle.setup(500, 600)

# setup the turtle
turtle.hideturtle()
turtle.fillcolor(COLOR)

# draw the left-side diamond first
turtle.begin_fill()

turtle.left(135)
turtle.forward(SIDE_LENGTH)

turtle.left(90)
turtle.forward(SIDE_LENGTH)

turtle.left(90)
turtle.forward(SIDE_LENGTH)

turtle.left(90)
turtle.forward(SIDE_LENGTH)

turtle.end_fill()

# draw the right-side diamond next
turtle.begin_fill()

turtle.forward(SIDE_LENGTH)

turtle.right(90)
turtle.forward(SIDE_LENGTH)

turtle.right(90)
turtle.forward(SIDE_LENGTH)

turtle.right(90)
turtle.forward(SIDE_LENGTH)

turtle.end_fill()

turtle.done()
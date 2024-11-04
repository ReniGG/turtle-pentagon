import turtle
import random

#set up the screen
ws = turtle.Screen()
ws.bgcolor("powder blue")

#create the turtle
will = turtle.Turtle()
will.speed(0)
will.shape("turtle")
will.pensize(5)


#function to draw the pentagon
def draw_pentagon(length, fill_color, pen_color):
    will.clear()
    will.fillcolor(fill_color)
    will.pencolor(pen_color)
    will.begin_fill()
    for _ in range(5):
        will.forward(length)
        will.right(72)
    will.end_fill()

# change the color randomly
def color_change(x, y):
    fill_color = (random.random(), random.random(), random.random())
    pen_color = (random.random(), random.random(), random.random())
    draw_pentagon (200, fill_color, pen_color)

ws.onscreenclick(color_change)

#draw the first pentagon 
color_change(0, 0)

turtle.done()
#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                          Turbo Turtle Etch-A-Sketch                           # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Classic Etch-A-Sketch created in Python with a turtle that has turbo mode.            #
# Background music is used for demo purposes and would require licensing.               #
# Feel free to change it to a song file you prefer.                                     #
#                                                                                       #
# Guide:                                                                                #
# cd into project folder: cd turbo_turtle                                               #
# Install Pygame to use their audio mixer for music: pip install pygame                 #
# turn your music volume up slightly                                                    #
# Launch by clicking run button in top right in VSCode or: py -3 main.py                #
#                                                                                       #
# Turtle Navigation:                                                                    #
# enter key = go/turbo, spacebar = change color, use arrows keys to navigate            #
# Launch by clicking run button in top right in VSCode or: py -3 main.py                #
#########################################################################################

import turtle as t
from turtle import Turtle, Screen
import random
from tkinter import messagebox
from pygame import mixer

# background music
mixer.init()
mixer.music.load("clue_step_by_step.mp3")
mixer.music.play()


# if want fixed screen size possibly for mobile responsiveness
# t.setup(400, 500)

# General display settings
t.title(
    "Turbo Turtle Etch-A-Sketch || Go/Turbo [Enter] || Move/Tap Arrow Keys [🡅🡇🡄🡆] || Random Color [Spacebar] || Instructions [i]")
t.colormode(255)
t.bgcolor("lightgrey")
screen = t.Screen()


# Move turtle forward, back, left, right by pixel amount (10 = 10px)
def forward():
    turtle.forward(10)
    # Block Turtle From Going Off Screen
    x, y = turtle.position()
    if -width < x < width and -height < y < height:
        return
    turtle.undo()


def backward():
    turtle.backward(10)


def left():
    turtle.left(10)


def right():
    turtle.right(10)


# Block Turtle From Going Off Screen
screen = Screen()

width, height = screen.window_width() / 2, screen.window_height() / 2


# Go/Turbo moves turtle forward faster each time activated
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:
        turtle.penup()
        state_num = 1
    else:
        turtle.pendown()
        turtle.forward(2)
        state_num = 0
    screen.ontimer(advance_state_machine, 25)

    # Block Turtle From Going Off Screen
    x, y = turtle.position()
    if -width < x < width and -height < y < height:
        return
    turtle.undo()


# Block Turtle From Going Off Screen
screen = Screen()

width, height = screen.window_width() / 2, screen.window_height() / 2


# Clears drawing and resets turtle's position
def clear_drawing():
    turtle.penup()
    turtle.clear()
    turtle.home()
    turtle.pendown()  # Keeps pencolor set by user


# activates draw mode
def no_drawing_mode():
    turtle.penup()


def draw_mode():
    turtle.pendown()


# adjust turtle width 1 to 10
def set_width():
    requested_width = screen.numinput('Width',
                                      'Width Amount <1 to 10>')
    if 1 <= requested_width <= 10:
        turtle.width(int(requested_width))
    else:
        messagebox.showwarning("Invalid Entry",
                               "Please enter value 1 to 10"
                               "Press 'w' to try again")


# randomly change color
def random_color_mode():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    turtle.color(rgb)


# instruction guide
def show_instructions():
    messagebox.showinfo('How to play:\n',
                        "'[Enter]' Go/Turbo\n"
                        "🡅 Forward\n"
                        "🡇 Backward\n"
                        "🡄 Left\n"
                        "🡆 Right\n"
                        "'[Space]' Random Color\n"
                        "'w' Pen Width\n"
                        "'c' Clear Drawing\n"
                        "'e' Enable Drawing Mode\n"
                        "'d' Disable Drawing Mode\n"
                        )


# icon/cursor
turtle = t.Turtle()
turtle.shape('turtle')
screen = t.Screen()

# on screen key listeners
screen.listen()

# Basic Functionalities
screen.onkeypress(forward, 'Up')
screen.onkeypress(backward, 'Down')
screen.onkeypress(right, 'Right')
screen.onkeypress(left, 'Left')
screen.onkeypress(random_color_mode, 'space')
screen.onkeypress(advance_state_machine, 'Return')
screen.onkeypress(set_width, 'w')
screen.onkeypress(clear_drawing, 'c')

# Other Functionality
screen.onkeypress(show_instructions, 'i')
screen.onkeypress(no_drawing_mode, 'd')
screen.onkeypress(draw_mode, 'e')

screen.mainloop()
screen.exitonclick()

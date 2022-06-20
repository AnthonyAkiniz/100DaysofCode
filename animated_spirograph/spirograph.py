#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                          Animated Spirograph                                  # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Python script that generates an animated spirograph using Turtle Graphics.            #
# documentation: https://docs.python.org/3/library/turtle.html                          #
#                                                                                       #
# Guide:                                                                                #
# Launch by clicking run button in top right in VSCode or: py -3 spirograph.py          #
#########################################################################################

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

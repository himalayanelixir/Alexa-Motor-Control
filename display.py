# Copyright 2020 Harlen Bains
# linted using pylint
# formatted using black
"""This script takes in one agrgument and then displays it on a InkyPhat
display"""
import sys
from PIL import Image, ImageFont, ImageDraw  # pylint: disable=import-error
from font_fredoka_one import FredokaOne  # pylint: disable=import-error
from inky import InkyPHAT  # pylint: disable=import-error


def print_text(text):
    """Displays text that is passed as an argument"""
    inky_display = InkyPHAT("yellow")
    inky_display.set_border(inky_display.WHITE)
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FredokaOne, 30)
    try:
        message = text
    except IndexError:
        message = "No Message"
    width, height = font.getsize(message)
    x_axis = (inky_display.WIDTH / 2) - (width / 2)
    y_axis = (inky_display.HEIGHT / 2) - (height / 2)
    draw.text((x_axis, y_axis), message, inky_display.YELLOW, font)
    inky_display.set_image(img)
    inky_display.show()


if __name__ == "__main__":
    print_text(str(sys.argv[1]))

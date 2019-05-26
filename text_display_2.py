###
#
# Lock screen
#   - requires user to input "lock_screen.c_c_c_combo" to equal "lock_screen.passfrase"
#
# TODO:
#   - clear up imports
#   - find a better solution for "wrap_text"
#   - prevent going off the bottom of the screen
#
###
import os
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from button_layout import button_A, button_B, button_C, button_U, button_D, button_L, button_R
from luma.core.render import canvas
from luma.core.virtual import terminal
from get_device import get_device
from PIL import ImageFont
import textwrap
import time

class lock_screen :

# Variables TODO: establish a better place for these
    lock_screen.fontname = "ProggyTiny.ttf"
    lock_screen.fontsize = 16
    lock_screen.c_c_c_combo = []
    lock_screen.passfrase = ["U", "U", "D", "D", "R", "R", "B", "A"]
    lock_screen.buttons_pressed = ""

    def wrap_text(text, row = 0) :
        with canvas(device) as draw :
            lines_newline = text.splitlines()
            y_text = row * 10
            for each_line in lines_newline :
                lines = textwrap.wrap(each_line, width=21)
                if len(lines) > 1 :
                    for line in lines :
                        draw.text((0, y_text), line, font=font, fill="white")
                        y_text += 10
                else :
                    draw.text((0, y_text), lines[0], font=font, fill="white")
                y_text += 10

    def make_font(name, size) :
        font_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), 'fonts', name))
        return ImageFont.truetype(font_path, size)

    font = make_font(lock_screen.fontname, lock_screen.fontsize)

# main lock script. TODO: figure out global bs
    def padlock(device, font, wrap_text) : #, lock_screen.passfrase, lock_screen.c_c_c_combo, lock_screen.buttons_pressed) :

    # Code submitted
        if not button_C.value :
            if lock_screen.c_c_c_combo == lock_screen.passfrase :
                return False
            else :
                wrap_text("fuck you")
                time.sleep(5)
                lock_screen.c_c_c_combo = []
                lock_screen.buttons_pressed = ""
                return True
    # Not Submitted
        else :
            if not button_U.value :
                lock_screen.c_c_c_combo.append("U")
                lock_screen.buttons_pressed = lock_screen.buttons_pressed + "*"
                time.sleep(.2)
            elif not button_D.value :
                lock_screen.c_c_c_combo.append("D")
                lock_screen.buttons_pressed = lock_screen.buttons_pressed + "*"
                time.sleep(.2)
            elif not button_L.value :
                lock_screen.c_c_c_combo.append("L")
                lock_screen.buttons_pressed = lock_screen.buttons_pressed + "*"
                time.sleep(.2)
            elif not button_R.value :
                lock_screen.c_c_c_combo.append("R")
                lock_screen.buttons_pressed = lock_screen.buttons_pressed + "*"
                time.sleep(.2)
            elif not button_A.value :
                lock_screen.c_c_c_combo.append("A")
                lock_screen.buttons_pressed = lock_screen.buttons_pressed + "*"
                time.sleep(.2)
            elif not button_B.value :
                lock_screen.c_c_c_combo.append("B")
                lock_screen.buttons_pressed = lock_screen.buttons_pressed + "*"
                time.sleep(.2)
            else :
                wrap_text("Enter Password:\n" + lock_screen.buttons_pressed)

            return True

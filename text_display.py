###
#
# Lock screen
#   - requires user to input "c_c_c_combo" to equal "passfrase"
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
from text_display_2 import lock_screen

    #def main() :
device = get_device()

locked = True

    # Device locked
while locked :
    locked = lock_screen.padlock(device, font, wrap_text) #, passfrase, c_c_c_combo, buttons_pressed)

    # Device unlocked
wrap_text("Yay! you did it!")
time.sleep(1)
wrap_text("Yay! you did it!\nbut still fuck you")
time.sleep(5)

    #main()

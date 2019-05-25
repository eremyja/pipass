import os
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from button_layout import button_A, button_B, button_C, button_U, button_D, button_L, button_R
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from luma.core.virtual import terminal
from PIL import ImageFont

def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)

while True:
    for fontname, size in [(None, None), ("tiny.ttf", 6), ("ProggyTiny.ttf", 16), ("creep.bdf", 16), ("miscfs_.ttf", 12), ("FreePixel.ttf", 12), ('ChiKareGo.ttf', 16)]:
        font = make_font(fontname, size) if fontname else None
        term = terminal(device, font)

        if button_U.value :
            term.println("Pressing Up")
        if button_D.value :
            term.println("Pressing Down")
        if button_L.value :
            term.println("Pressing Left")
        if button_R.value :
            term.println("Pressing Right")
        if button_A.value :
            term.println("Pressing A")
        if button_B.value :
            term.println("Pressing B")
        else :
            term.println("Waiting for you to press something")

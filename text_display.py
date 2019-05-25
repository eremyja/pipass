import os
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from button_layout import button_A, button_B, button_C, button_U, button_D, button_L, button_R
#from luma.core.interface.serial import i2c
from luma.core.render import canvas
#from luma.oled.device import ssd1306
#from luma.core.virtual import terminal
from get_device import get_device
from PIL import ImageFont
import textwrap

#serial = i2c(port=1, address=0x3C)
#device = ssd1306(serial)

fontname = "ProggyTiny.ttf"
fontsize = 16
c_c_c_combo = []
passfrase = ["U", "U", "D", "D", "R", "R", "B", "A"]
buttons_pressed = ""


def make_font(name, size) :
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)

def text_input_test(device) :
    global buttons_pressed
    #while True:
        #for fontname, size in [(None, None), ("tiny.ttf", 6), ("ProggyTiny.ttf", 16), ("creep.bdf", 16), ("miscfs_.ttf", 12), ("FreePixel.ttf", 12), ('ChiKareGo.ttf', 16)]:
    font = make_font(fontname, fontsize) if fontname else None
            #term = terminal(device, font)
    with canvas(device) as draw:

        def wrap_text(text) :
            lines = textwrap.wrap(text, width=21)
            y_text = 0
            for line in lines:
                draw.text((21, y_text), line, font=font, fill="white")
                y_text += 10



        wrap_text("Enter Password:\n" + buttons_pressed)

        if not button_U.value :
            c_c_c_combo.append("U")
            buttons_pressed = buttons_pressed + "*"
        elif not button_D.value :
            c_c_c_combo.append("D")
            buttons_pressed = buttons_pressed + "*"
        elif not button_L.value :
            c_c_c_combo.append("L")
            buttons_pressed = buttons_pressed + "*"
        elif not button_R.value :
            c_c_c_combo.append("R")
            buttons_pressed = buttons_pressed + "*"
        elif not button_A.value :
            c_c_c_combo.append("A")
            buttons_pressed = buttons_pressed + "*"
        elif not button_B.value :
            c_c_c_combo.append("B")
            buttons_pressed = buttons_pressed + "*"
        elif not button_C.value :
            if c_c_c_combo == passfrase :
                wrap_text("Yay! you did it!")
            else :
                wrap_text("fuck you")
                c_c_c_combo = []

#        if not button_U.value :
#            wrap_text("Up")
#        elif not button_D.value :
#            wrap_text("Down")
#        elif not button_L.value :
#            wrap_text("Left")
#        elif not button_R.value :
#            wrap_text("Right")
#        elif not button_C.value :
#            wrap_text("Center")
#        elif not button_A.value :
#            wrap_text("A")
#        elif not button_B.value :
#            wrap_text("B")
#        else :
#            wrap_text("Press Something")

def main() :
    while True :
        text_input_test(device)

if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass

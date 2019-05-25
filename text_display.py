import os
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from button_layout import button_A, button_B, button_C, button_U, button_D, button_L, button_R
#from luma.core.interface.serial import i2c
from luma.core.render import canvas
#from luma.oled.device import ssd1306
from luma.core.virtual import terminal
from get_device import get_device
from PIL import ImageFont
import textwrap
import time

#serial = i2c(port=1, address=0x3C)
#device = ssd1306(serial)

fontname = "ProggyTiny.ttf"
fontsize = 16
c_c_c_combo = []
passfrase = ["U", "U", "D", "D", "R", "R", "B", "A"]
buttons_pressed = ""

def wrap_text(text, row = 0) :
    with canvas(device) as draw :
        lines_newline = text.splitlines()
        for each_line in lines_newline :
            lines = textwrap.wrap(each_line, width=21)
            y_text = row * 10
            for line in lines :
                draw.text((0, y_text), line, font=font, fill="white")
                y_text += 10

def make_font(name, size) :
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)

font = make_font(fontname, fontsize)

def text_input_test(device, font, wrap_text) : #, passfrase, c_c_c_combo, buttons_pressed) :
    global passfrase
    global c_c_c_combo
    global buttons_pressed
    #with canvas(device) as draw :


    #while True:
        #for fontname, size in [(None, None), ("tiny.ttf", 6), ("ProggyTiny.ttf", 16), ("creep.bdf", 16), ("miscfs_.ttf", 12), ("FreePixel.ttf", 12), ('ChiKareGo.ttf', 16)]:
    #font = make_font(fontname, fontsize) if fontname else None
            #term = terminal(device, font)

    if not button_C.value :
        if c_c_c_combo == passfrase :
            #with canvas(device) as draw :
            #draw.rectangle(device.bounding_box, fill="black")
            #wrap_text("Yay! you did it!")
            #time.sleep(5)
            #c_c_c_combo = []
            #buttons_pressed = ""
            return False
        else :
            #with canvas(device) as draw :
            #draw.rectangle(device.bounding_box, fill="black")
            wrap_text("fuck you")
            time.sleep(5)
            c_c_c_combo = []
            buttons_pressed = ""
            return True
    else :
    #with canvas(device) as draw:
#            def wrap_text(text, row = 0) :
#                lines = textwrap.wrap(text, width=21)
#                y_text = row * 10
#                for line in lines:
#                    draw.text((21, y_text), line, font=font, fill="white")
#                    y_text += 10

        #wrap_text("Enter Password:")
        #wrap_text(buttons_pressed, 1)

        if not button_U.value :
            c_c_c_combo.append("U")
            buttons_pressed = buttons_pressed + "*"
            time.sleep(.2)
        elif not button_D.value :
            c_c_c_combo.append("D")
            buttons_pressed = buttons_pressed + "*"
            time.sleep(.2)
        elif not button_L.value :
            c_c_c_combo.append("L")
            buttons_pressed = buttons_pressed + "*"
            time.sleep(.2)
        elif not button_R.value :
            c_c_c_combo.append("R")
            buttons_pressed = buttons_pressed + "*"
            time.sleep(.2)
        elif not button_A.value :
            c_c_c_combo.append("A")
            buttons_pressed = buttons_pressed + "*"
            time.sleep(.2)
        elif not button_B.value :
            c_c_c_combo.append("B")
            buttons_pressed = buttons_pressed + "*"
            time.sleep(.2)
        else :
            wrap_text("Enter Password:\n" + buttons_pressed)
            #wrap_text(buttons_pressed, 1)
        return True
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
    #font = make_font(fontname, fontsize)
    locked = True
    #with canvas(device) as draw :
        #wrap_text("Enter Password:")
        #wrap_text(buttons_pressed, 1)
        #time.sleep(1)
    while locked :
        #with canvas(device) as draw:

        locked = text_input_test(device, font, wrap_text) #, passfrase, c_c_c_combo, buttons_pressed)

    #with canvas(device) as draw :
    wrap_text("Yay! you did it!")
    time.sleep(1)
    wrap_text("Yay! you did it!\n but still fuck you")
    time.sleep(5)

if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass

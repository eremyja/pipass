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

def make_font(name, size) :
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)

def text_input_test(device) :
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

        if not button_U.value :
            draw.text((0,0), "fuck you", font=font, fill="white")
        elif not button_D.value :
            draw.text((0,0), "fuck you", font=font, fill="white")
        elif not button_L.value :
            draw.text((0,0), "fuck you", font=font, fill="white")
        elif not button_R.value :
            draw.text((0,0), "fuck you", font=font, fill="white")
        elif not button_C.value :
            draw.text((0,0), "fuck you", font=font, fill="white")
        elif not button_A.value :
            draw.text((0,0), "fuck you", font=font, fill="white")
        elif not button_B.value :
            draw.text((0,0), "fuck you", font=font, fill="white")
        else :
            wrap_text("123456789012345678901234567890")
            #draw.text((0,0), "Press something", font=font, fill="white")
            #draw.text((0,10), "Press something", font=font, fill="white")
            #draw.text((0,20), "Press something", font=font, fill="white")
            #draw.text((0,30), "Press something", font=font, fill="white")
            #draw.text((0,40), "Press something", font=font, fill="white")
            #draw.text((0,50), "Press something", font=font, fill="white")

def main() :
    while True :
        text_input_test(device)

if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass

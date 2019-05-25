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

#serial = i2c(port=1, address=0x3C)
#device = ssd1306(serial)

fontname = "ProggyTiny.ttf"
fontsize = 12

def make_font(name, size) :
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)
def text_input_test(device) :
    #while True:
        #for fontname, size in [(None, None), ("tiny.ttf", 6), ("ProggyTiny.ttf", 16), ("creep.bdf", 16), ("miscfs_.ttf", 12), ("FreePixel.ttf", 12), ('ChiKareGo.ttf', 16)]:
    font = make_font(fontname, fontsize) if fontname else None
            #term = terminal(device, font)

    if not button_U.value :
        draw.text((0,0), "Pressing Up", font=font, fill="white")
    elif not button_D.value :
        draw.text((0,0), "Pressing Down", font=font, fill="white")
    elif not button_L.value :
        draw.text((0,0), "Pressing Left", font=font, fill="white")
    elif not button_R.value :
        draw.text((0,0), "Pressing Right", font=font, fill="white")
    elif not button_A.value :
        draw.text((0,0), "Pressing A", font=font, fill="white")
    elif not button_B.value :
        draw.text((0,0), "Pressing B", font=font, fill="white")
    else :
        draw.text((0,0), "Waiting for you to press something", font=font, fill="white")

def main() :
    while True :
        text_input_test(device)

if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass

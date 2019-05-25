import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from button_layout import button_A, button_B, button_C, button_U, button_D, button_L, button_R
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

with canvas(device) as draw:
    while True:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((30, 40), "Hello World", fill="white")
#        if button_U.value: # button is released
#            draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0)  #Up
#        else: # button is pressed:
#            draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=1)  #Up filled

#        if button_L.value: # button is released
#            draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0)  #left
#        else: # button is pressed:
#            draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=1)  #left filled

#        if button_R.value: # button is released
#            draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0) #right
#        else: # button is pressed:
#            draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=1) #right filled

#        if button_D.value: # button is released
#            draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0) #down
#        else: # button is pressed:
#            draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=1) #down filled

#        if button_C.value: # button is released
#            draw.rectangle((20, 22, 40, 40), outline=255, fill=0) #center
#        else: # button is pressed:
#            draw.rectangle((20, 22, 40, 40), outline=255, fill=1) #center filled

#        if button_A.value: # button is released
#            draw.ellipse((70, 40, 90, 60), outline=255, fill=0) #A button
#        else: # button is pressed:
#            draw.ellipse((70, 40, 90, 60), outline=255, fill=1) #A button filled

#        if button_B.value: # button is released
#            draw.ellipse((100, 20, 120, 40), outline=255, fill=0) #B button
#        else: # button is pressed:
#            draw.ellipse((100, 20, 120, 40), outline=255, fill=1) #B button filled

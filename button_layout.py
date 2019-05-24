###
# Requires:
import board
from digitalio import DigitalInOut, Direction, Pull
###

# Input pins:
def button_A() :
    button_A = DigitalInOut(board.D5)
    button_A.direction = Direction.INPUT
    button_A.pull = Pull.UP

def button_B() :
    button_B = DigitalInOut(board.D6)
    button_B.direction = Direction.INPUT
    button_B.pull = Pull.UP

def button_L() :
    button_L = DigitalInOut(board.D27)
    button_L.direction = Direction.INPUT
    button_L.pull = Pull.UP

def button_R() :
    button_R = DigitalInOut(board.D23)
    button_R.direction = Direction.INPUT
    button_R.pull = Pull.UP

def button_U() :
    button_U = DigitalInOut(board.D17)
    button_U.direction = Direction.INPUT
    button_U.pull = Pull.UP

def button_D() :
    button_D = DigitalInOut(board.D22)
    button_D.direction = Direction.INPUT
    button_D.pull = Pull.UP

def button_C() :
    button_C = DigitalInOut(board.D4)
    button_C.direction = Direction.INPUT
    button_C.pull = Pull.UP

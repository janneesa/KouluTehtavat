import micropython
import ssd1306
import time
import machine
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

SW0_PIN = 7
SW1_PIN = 8
SW2_PIN = 9

OLED_WIDTH = 128
OLED_HEIGHT = 64

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

right_button = machine.Pin(SW0_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
left_button = machine.Pin(SW2_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
reset_button = machine.Pin(SW1_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

micropython.alloc_emergency_exception_buf(200)

going_right = True

X_COORD = 0
Y_COORD = 32


def go_right():
    global X_COORD, Y_COORD  # Declare X_COORD and Y_COORD as global
    oled.pixel(X_COORD, Y_COORD, 1)
    oled.show()
    X_COORD += 1


def go_left():
    global X_COORD, Y_COORD  # Declare X_COORD and Y_COORD as global
    oled.pixel(X_COORD, Y_COORD, 1)
    oled.show()
    X_COORD -= 1


while True:
    if going_right:
        go_right()
        if X_COORD >= OLED_WIDTH:
            going_right = False
    if not going_right:
        go_left()
        if X_COORD <= 0:
            going_right = True

    if not left_button.value():
        Y_COORD += 1
    elif not right_button.value():
        Y_COORD -= 1
    elif not reset_button.value():
        oled.fill(0)
        X_COORD = 0
        Y_COORD = 32
        going_right = True

    time.sleep(0.01)


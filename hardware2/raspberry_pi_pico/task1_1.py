import micropython
import ssd1306
import fifo
import time
import machine
from machine import Pin, UART, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C


SW0_PIN = 7
SW2_PIN = 9

OLED_WIDTH = 128
OLED_HEIGHT = 64

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

right_button = machine.Pin(SW0_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
left_button = machine.Pin(SW2_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

ufo_position = OLED_WIDTH // 2

micropython.alloc_emergency_exception_buf(200)



def draw_ufo(x):
    oled.fill(0)
    oled.text("<=>", x, OLED_HEIGHT - 8)
    oled.show()


#rb = fifo.Fifo(50)
#print('I am test.py')

#if rb.empty():
    #print('Fifo is empty')

led = Pin("LED", Pin.OUT)

while True:
    draw_ufo(ufo_position)

    if not right_button.value():
        if ufo_position > 0:
            ufo_position -= 5
        time.sleep(0.01)

    if not left_button.value():
        if ufo_position < OLED_WIDTH - 24:
            ufo_position += 5
        time.sleep(0.01)



import micropython
import ssd1306
import fifo
import time
import machine
from machine import Pin, UART, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C
from filefifo import Filefifo



led = Pin("LED", Pin.OUT)

SW0_PIN = 7
SW2_PIN = 9

OLED_WIDTH = 128
OLED_HEIGHT = 64

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

right_button = machine.Pin(SW0_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
left_button = machine.Pin(SW2_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

micropython.alloc_emergency_exception_buf(200)


data = Filefifo(10, name='capture_250Hz_01.txt')
signal_data = []

value = 0

for i in range(2500):
    signal_data.append(data.get())

min_value = min(signal_data)
max_value = max(signal_data)

print("Min: ", min_value)
print("Max: ", max_value)

scaled_signal = []

for i in signal_data:
    value = (i - min_value) / (max_value - min_value) * 100
    scaled_signal.append(value)

for value in scaled_signal:
    print(value)


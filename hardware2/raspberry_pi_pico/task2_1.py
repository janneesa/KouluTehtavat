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


# Function to find positive peaks using slope inspection
def find_positive_peaks(signal_data):
    peaks = []
    prev_slope = 0

    for i in range(1, len(signal_data)):
        slope = signal_data[i] - signal_data[i - 1]

        # Check if slope turns from positive to negative
        if slope < 0 and prev_slope > 0:
            peaks.append(i - 1)

        prev_slope = slope

    return peaks


for i in range(5000):
    signal_data.append(data.get())

peaks = find_positive_peaks(signal_data)

for i in range(len(peaks) - 1):
    interval_samples = peaks[i + 1] - peaks[i]
    interval_seconds = interval_samples / 250  # sampling rate
    print(f"Peak-to-peak interval {i + 1}: {interval_samples} samples, {interval_seconds:.3f} seconds")

if len(peaks) >= 2:
    average_interval_samples = sum(peaks[i + 1] - peaks[i] for i in range(len(peaks) - 1)) / (len(peaks) - 1)
    frequency = 250 / average_interval_samples
    print(f"Frequency of the signal: {frequency:.2f} Hz")
else:
    print("Insufficient peaks to calculate frequency.")



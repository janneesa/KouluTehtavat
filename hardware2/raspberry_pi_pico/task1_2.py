import machine
import ssd1306
import time

SW0_PIN = 7
SW2_PIN = 9

OLED_WIDTH = 128
OLED_HEIGHT = 64

i2c = machine.I2C(1, scl=machine.Pin(15), sda=machine.Pin(14), freq=400000)
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)


def draw_text(text_lines):
    oled.fill(0)
    for i, line in enumerate(text_lines):
        oled.text(line, 0, i * 10)
    oled.show()

text_lines = []

while True:
    user_input = input()
    text_lines.append(user_input)

    if len(text_lines) * 10 > OLED_HEIGHT:
        text_lines.pop(0)

    draw_text(text_lines)

    time.sleep(0.1)


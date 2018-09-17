import time
import board
import digitalio
import neopixel
import random

# define buttonA
button_a = digitalio.DigitalInOut(board.D4)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN

# define buttonB
button_b = digitalio.DigitalInOut(board.D5)
button_b.direction = digitalio.Direction.INPUT
button_b.pull = digitalio.Pull.DOWN

# define neopixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05, auto_write = True)
pixels.fill((0, 0, 0))
pixels.show()


while True:
# change color counter clockwise if buttonA is pressed
    if button_a.value:
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        for i in range(0,10,1):
            pixels[i] = (r,g,b)
            time.sleep(0.1)
# if buttonA is released, stop changing color
            if button_a.value == False:
                break
# change color clockwise if buttonB is pressed
    if button_b.value:
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        for i in range(9,-1,-1):
            pixels[i] = (r,g,b)
            time.sleep(0.1)
# if buttonA is released, stop changing color
            if button_b.value == False:
                break

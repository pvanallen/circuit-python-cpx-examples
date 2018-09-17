import time
import board
import digitalio
import neopixel

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

# initialization half green half red
for i in range(10):
    if i < 5:
        pixels[i] = (0,255,0)
    else:
        pixels[i] = (255,0,0)

# some variables for check button status

# record which neopixel should be green if buttonA be pressed (nextred = nextgreen - 1)
nextgreen = 5

# record previous button status
prea = False
preb = False

# click signal for each button
a_clicked = False
b_clicked = False

while True:

    # check if buttonA is clicked
    if prea == False and button_a.value == True:
        prea = button_a.value
        a_clicked = True
    elif prea == True and button_a.value == False:
        prea = button_a.value
    else:
        a_clicked = False

    # check if buttonB is clicked
    if preb == False and button_b.value == True:
        preb = button_b.value
        b_clicked = True
    elif preb == True and button_b.value == False:
        preb = button_b.value
    else:
        b_clicked = False

    # change neopixel color
    if nextgreen != 0 and nextgreen != 10:
        if a_clicked:
            pixels[nextgreen] = (0,255,0)
            nextgreen += 1

        if b_clicked:
            pixels[nextgreen-1] = (255,0,0)
            nextgreen -= 1
    # if someone win then reset color
    else:
        for i in range(10):
            pixels[i] = (255,0,0)
        for i in range(10):
            pixels[i] = (0,255,0)
        for i in range(10):
            pixels[i] = (0,0,255)
        for i in range(10):
            if i < 5:
                pixels[i] = (0,255,0)
            else:
                pixels[i] = (255,0,0)

        nextgreen = 5

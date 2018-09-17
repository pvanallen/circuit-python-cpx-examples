import time
import board
import digitalio
import simpleio
import audioio
import touchio
import neopixel
import math
import random


# define neopixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = .05, auto_write = True)


# define touch pad 1 - 6
touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A3)
touch4 = touchio.TouchIn(board.A4)
touch5 = touchio.TouchIn(board.A5)
touch6 = touchio.TouchIn(board.A6)

# enable speaker
speakerswitch = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speakerswitch.direction = digitalio.Direction.OUTPUT
speakerswitch.value = True

# define speaker
speaker = audioio.AudioOut(board.SPEAKER)

# load audio data
data1 = open("bomb.wav", "rb")
data2 = open("begin.wav", "rb")
data3 = open("safe.wav", "rb")
sound1 = audioio.WaveFile(data1)
sound2 = audioio.WaveFile(data2)
sound3 = audioio.WaveFile(data3)

# hide bomb somewhere
bomb = random.randrange(1,6)

# the initial light effects of the game
def restartled():
    pixels[0] = (255,255,255)
    pixels[1] = (0,0,0)
    pixels[2] = (255,255,255)
    pixels[3] = (0,0,0)
    pixels[4] = (255,255,255)
    pixels[5] = (255,255,255)
    pixels[6] = (0,0,0)
    pixels[7] = (255,255,255)
    pixels[8] = (0,0,0)
    pixels[9] = (255,255,255)

# the sound and light effects of explosion. And restart the game after the effects
def bomblight():
    speaker.play(sound1)
    for i in range(10):
        pixels[i] = (255,0,0)
    time.sleep(0.5)
    for i in range(10):
        pixels[i] = (255,100,0)
    time.sleep(0.5)
    for i in range(10):
        pixels[i] = (255,255,0)
    time.sleep(0.5)
    for i in range(10):
        pixels[i] = (255,0,0)
    time.sleep(1)
# restart the game
    restartled()
    time.sleep(0.5)
    speaker.play(sound2)
# hide bomb somewhere
    return random.randrange(1,6)

# initiate neopixels color
restartled()

# play the opening sound
speaker.play(sound2)



while True:

# assign neopixel number to touchpad number
    neopixelnum = {
        1:5,
        2:7,
        3:9,
        4:0,
        5:2,
        6:4
    }
    
#if the pin is touched
    if touch1.value:
        if bomb == 1:
            bomb = bomblight()
        else:
            print("A1")
            speaker.play(sound3)
            pixels[neopixelnum[1]] = (0,255,0)
    if touch2.value:
        if bomb == 2:
            bomb = bomblight()
        else:
            print("A2")
            speaker.play(sound3)
            pixels[neopixelnum[2]] = (0,255,0)
    if touch3.value:
        if bomb == 3:
            bomb = bomblight()
        else:
            print("A3")
            speaker.play(sound3)
            pixels[neopixelnum[3]] = (0,255,0)
    if touch4.value:
        if bomb == 4:
            bomb = bomblight()
        else:
            print("A1")
            speaker.play(sound3)
            pixels[neopixelnum[4]] = (0,255,0)
    if touch5.value:
        if bomb == 5:
            bomb = bomblight()
        else:
            print("A5")
            speaker.play(sound3)
            pixels[neopixelnum[5]] = (0,255,0)
    if touch6.value:
        if bomb == 6:
            bomb = bomblight()
        else:
            print("A6")
            speaker.play(sound3)
            pixels[neopixelnum[6]] = (0,255,0)


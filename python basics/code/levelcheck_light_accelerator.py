import time
import board
import digitalio
import simpleio
import neopixel
import math
import adafruit_lis3dh
import busio

# get data from accelerometer
if hasattr(board, 'ACCELEROMETER_SCL'):
    i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
    int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)

# set accelerometer range (2G, 4G, 8G, 16G)
lis3dh.range = adafruit_lis3dh.RANGE_2_G

# define neopixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = .05, auto_write = True)

# initiate neopixels color
for i in range(10):
    pixels[i] = (0,0,0)

# loop forever
while True:
# read acceleration data
    x, y, z = lis3dh.acceleration

# standardlize acceleration data
    dx = x/9.8
    dy = y/9.8
    dz = z/9.8

# caculate tilt direction the map to 0-12
# 0,12->right  6->left  3->up  9->down
    leveltan = simpleio.map_range(math.atan2(dy,dx),-math.pi,math.pi,0,12)

# assign direction number to neopixel number
# note: direction 3 and 9 don't have neopixel, assign them to the adjacent neopixel)
    neopixelnum = {
        0:7,
        1:8,
        2:9,
        3:0,
        4:0,
        5:1,
        6:2,
        7:3,
        8:4,
        9:5,
        10:5,
        11:6,
        12:7
    }
# if level, set all the neopixels to green
    if math.fabs(dy) < 0.05 and math.fabs(dx) < 0.05:
        for i in range(10):
            pixels[i] = (0,225,0)
    else:
        for i in range(10):
# set the tilt direction neopixel to red
            if i == neopixelnum[round(leveltan)]:
                pixels[i] = (225,0,0)
# set the adjacent neopixels to yellow
            elif i-1 == neopixelnum[round(leveltan)] or i+1 == neopixelnum[round(leveltan)]:
                pixels[i] = (150,150,0)
# turn off the rest neopixels
            else:
                pixels[i] = (0,0,0)

    print(x,y,z)
    time.sleep(0.01)

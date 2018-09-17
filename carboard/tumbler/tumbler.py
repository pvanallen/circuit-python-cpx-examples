import time
import board
import digitalio
import simpleio
import pulseio
import neopixel
import adafruit_motor.servo
import adafruit_lis3dh
import busio


# define neopixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05, auto_write = True)

# turn off the neopixels at the beginning
for i in range(10):
    pixels[i] = (0,0,0)
 
# create a PWMOut object on Pin A1.(2**15 = 32768)
pwm = pulseio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
 
# Create a servo object, servo.
servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2250)


# get data from accelerometer
if hasattr(board, 'ACCELEROMETER_SCL'):
    i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
    int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)

# set accelerometer range (2G, 4G, 8G, 16G)
lis3dh.range = adafruit_lis3dh.RANGE_2_G

# neopixels angle indicator function
def ledcolor(num):
    if num < 4:
        for i in range(0,num,1):
            pixels[i] = (0,0,0)
        for i in range(num,5,1):
            pixels[i] = (255,255,0)
        for i in range(5,10,1):
            pixels[i] = (0,0,0)
    elif num > 5:
        for i in range(0,5,1):
            pixels[i] = (0,0,0)
        for i in range(5,num+1,1):
            pixels[i] = (255,255,0)
        for i in range(num+1,10,1):
            pixels[i] = (0,0,0)
    else:
        for i in range(0,4,1):
            pixels[i] = (0,0,0)
        for i in range(4,6,1):
            pixels[i] = (255,255,0)
        for i in range(6,9,1):
            pixels[i] = (0,0,0)            



while True:

# read acceleration data
    x, y, z = lis3dh.acceleration   
# standardlize acceleration data
    dx = x/9.8

# remap standaralized accelerationdata to axial rotation ratio
    rotationratio = simpleio.map_range(dx,-1,1,1,0)

# use acceleration data to controller servo
    servo.angle = 180*rotationratio
    
# neopixels angle indicator
    ledcolor(round(rotationratio*9))
        
    print(round(rotationratio*9))
    time.sleep(0.01)
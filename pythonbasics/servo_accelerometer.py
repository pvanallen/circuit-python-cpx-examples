import time
import board
import digitalio
import simpleio
import pulseio
import adafruit_motor.servo
import adafruit_lis3dh
import busio

# create a PWMOut object on Pin 13.(2**15 = 32768)
pwm = pulseio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
servo = adafruit_motor.servo.Servo(pwm, min_pulse=750, max_pulse=2250)

# get data from accelerometer
if hasattr(board, 'ACCELEROMETER_SCL'):
    i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
    int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)

# set accelerometer range (2G, 4G, 8G, 16G)
lis3dh.range = adafruit_lis3dh.RANGE_2_G

while True:

# read acceleration data
    x, y, z = lis3dh.acceleration
# standardlize acceleration data
    dx = x/9.8

# remap standaralized accelerationdata to axial rotation ratio
    rotationratio = simpleio.map_range(dx,-1,1,1,0)

    servo.angle = 180*rotationratio

    time.sleep(0.01)

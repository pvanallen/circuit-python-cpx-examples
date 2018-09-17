import time
import board
import digitalio
import simpleio
import audioio
import math
import array
import adafruit_lis3dh
import busio


# get data from accelerometer
if hasattr(board, 'ACCELEROMETER_SCL'):
    i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
    int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
    lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)

# set accelerometer range (2G, 4G, 8G, 16G)
lis3dh.range = adafruit_lis3dh.RANGE_4_G

# enable speaker
speakerswitch = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speakerswitch.direction = digitalio.Direction.OUTPUT
speakerswitch.value = True

# define speaker
speaker = audioio.AudioOut(board.SPEAKER)

# define playing function
def playtone(num):
# generate one period of sine wav
    frequency = 440
    length = 8000 // frequency
    sine_wave = array.array("h", [0] * length)

    for i in range(length):
        sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15))
    beep = audioio.RawSample(sine_wave)

# play the beeps different times (num)
    for i in range(num):
        if speaker.playing == False:
            speaker.play(beep, loop = True)
            time.sleep(0.3)
            speaker.stop()
# set the interval between beeps
        time.sleep(0.1)

# define stop playing function
def audiostop():
    if speaker.playing:
        speaker.stop()

# set parameter to check if the beep has been played
played = True

# check if the cube is shaking
def ifshake(a,b,c,pa,pb,pc):
# find the angle between two position of the circuit board
    cos = ((a*pa)+(b*pb)+(c*pc))/((math.sqrt(a**2+b**2+c**2))*(math.sqrt(pa**2+pb**2+pc**2)))
    print(math.degrees(math.acos(cos)))
# set the threshold of shaking (now is 25 degrees)
    if math.degrees(math.acos(cos)) > 25:
        return True
    else:
        return False




while True:

# read acceleration data
# standardlize acceleration data
    x, y, z = lis3dh.acceleration
    dx = x/9.8
    dy = y/9.8
    dz = z/9.8

# read acceleration data (after 0.01 secs)
# standardlize acceleration data
    time.sleep(0.01)
    x, y, z = lis3dh.acceleration
    pdx = x/9.8
    pdy = y/9.8
    pdz = z/9.8


# if the cube is not shaking and the beep has not been played
    if ifshake(dx,dy,dz,pdx,pdy,pdz) == False and played == False:
        time.sleep(1.5)
# read current position data
        x, y, z = lis3dh.acceleration
        cx = x/9.8
        cy = y/9.8
        cz = z/9.8
# play beeps if the cube is horizontal
        if cz > 0.85:
            playtone(1)
            played = True
        elif cz < -0.85:
            playtone(2)
            played = True
        elif cx > 0.85:
            playtone(3)
            played = True
        elif cx < -0.85:
            playtone(4)
            played = True
        elif cy > 0.85:
            playtone(5)
            played = True
        elif cy < -0.85:
            playtone(6)
            played = True
# play nothing is tilted
        else:
            played = True
            audiostop()
# if the cube is shaking
    elif ifshake(dx,dy,dz,pdx,pdy,pdz):
        played = False
        audiostop()

    print(played,ifshake(dx,dy,dz,pdx,pdy,pdz))
    time.sleep(0.05)

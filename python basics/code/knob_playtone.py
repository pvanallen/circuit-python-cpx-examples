import time
import board
import analogio
import digitalio
import math
import array
import audioio

# connect knob to pin A1
knob = analogio.AnalogIn(board.A1)

# record previous knob data to check if the knob has rotated
prepin = 0

# enable speaker
speakerswitch = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speakerswitch.direction = digitalio.Direction.OUTPUT
speakerswitch.value = True

# define speaker
speaker = audioio.AudioOut(board.SPEAKER)

# generate one period of sine wav (C,D,E,F)
frequency = array.array("i",[261,293,329,349])
length = 8000 // frequency[num-1]
sine_wave = array.array("h", [0] * length)

for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15))
sound = audioio.RawSample(sine_wave)

# define playing function
def playtone(num):
# play the sound
    if speaker.playing == False:
        speaker.play(sound, loop = True)

# transform the knob data from 0-65536 to 0-4
def getdata(pin):
    return (pin.value*4) / 65536

while True:
# check if the knob has rotated
# if the knob enters a new section, then stop the old tone and play a new tone
    if prepin == int(getdata(knob)):
        playtone(int(getdata(knob)))
    else:
        speaker.stop()
        prepin = int(getdata(knob))

    print("Analog Voltage: %f" % int(getdata(knob)))
    time.sleep(0.1)

import time
import board
import audioio
import digitalio
import math
import array
import touchio


# enable speaker
speakerswitch = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speakerswitch.direction = digitalio.Direction.OUTPUT
speakerswitch.value = True


# define speaker
speaker = audioio.AudioOut(board.SPEAKER)

# define playing function
def playtone(num):
    # generate one period of sine wav (C,D,E,F,G,A,B)
    frequency = array.array("i",[261,293,329,349,392,440,493])
    length = 8000 // frequency[num-1]
    sine_wave = array.array("h", [0] * length)

    for i in range(length):
        sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15))
    sound = audioio.RawSample(sine_wave)
    # play the sound
    if speaker.playing == False:
        speaker.play(sound, loop = True)

# define stop playing function
def audiostop():
    if speaker.playing:
        speaker.stop()

# define touch pad 1 - 7
touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A3)
touch4 = touchio.TouchIn(board.A4)
touch5 = touchio.TouchIn(board.A5)
touch6 = touchio.TouchIn(board.A6)
touch7 = touchio.TouchIn(board.A7)


# loop forever
while True:

    #if the pin is touched
    if touch1.value:
        print("A1")
        playtone(1)
    if touch2.value:
        print("A2")
        playtone(2)
    if touch3.value:
        print("A3")
        playtone(3)
    if touch4.value:
        print("A4")
        playtone(4)
    if touch5.value:
        print("A5")
        playtone(5)
    if touch6.value:
        print("A6")
        playtone(6)
    if touch7.value:
        print("A7")
        playtone(7)

    # stop playing if nothing is touched 
    if touch1.value == False and touch2.value == False and touch3.value == False and touch4.value == False and touch5.value == False and touch6.value == False and touch7.value == False:
        audiostop()

time.sleep(0.01)

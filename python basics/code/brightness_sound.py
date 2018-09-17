# put drum_cowbell.wav into CIRCUITPY root directory

import time
import board
import audioio
import digitalio
import analogio

# define lightsensor
lightsensor = analogio.AnalogIn(board.A8)

# enable speaker
speakerswitch = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speakerswitch.direction = digitalio.Direction.OUTPUT
speakerswitch.value = True

# define speaker
speaker = audioio.AudioOut(board.SPEAKER)

# load audio data
data1 = open("drum_cowbell.wav", "rb")
sound1 = audioio.WaveFile(data1)

while True:

    # play audio if environment is bright
    print(lightsensor.value)
    if lightsensor.value > 5000:
        if speaker.playing != True:
            speaker.play(sound1,loop = True)
    else:
        speaker.stop()

    time.sleep(0.01)
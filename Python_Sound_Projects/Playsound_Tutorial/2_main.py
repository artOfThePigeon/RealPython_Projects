# using simple audio to play a soundfile

import simpleaudio as sa

filename = 'airplane.mp3'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()

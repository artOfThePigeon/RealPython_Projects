# play a file using winsound in the standard python library.

import winsound

filename = 'airplane.wav'
winsound.PlaySound(filename, winsound.SND_FILENAME)

winsound.Beep(1000, 1000)

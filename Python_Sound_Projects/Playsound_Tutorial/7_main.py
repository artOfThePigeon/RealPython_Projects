# simple way to play audio file with pydub
from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_mp3('airplane.mp3')
play(sound)

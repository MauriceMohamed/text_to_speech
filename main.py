#program that read a string using gtts and plays it
#import the necessary packages
from gtts import gTTS

tts = gTTS(text='Hello World', lang='en')
tts.save("hello.mp3")
import random
import urllib
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

wey = "w"



import webbrowser
rang = 10
webbrowser.open('https://youtu.be/0miEnUJ2-jA')
time.sleep(1)
while(True):
#for i in range(rang):
    webbrowser.open('https://youtu.be/0miEnUJ2-jA')
    time.sleep(1)
    keyboard.press(Key.ctrl)
    keyboard.press(wey)
    keyboard.release(wey)
    keyboard.release(Key.ctrl)
    
    print("this worked")
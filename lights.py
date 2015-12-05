""" 
    Matan Uchen
    In my continous adventures with hardware and circuitry I decided to
    get in the Christmas spirit.  Button toggles christmas colored LEDs
    cause why not.

"""
from pygame import mixer
from gpiozero import LED, Button
import time

button = Button(4)

led1 = LED(5)  # GPIO 5
led2 = LED(6)  # GPIO 6
led3 = LED(12) # GPIO 12
led4 = LED(13) # GPIO 13

""" Easier to write a for loop """
leds = [led1, led2, led3, led4]

""" Initialize the lights """
def lights():
    led1.on()
    led3.on()
    led2.off()
    led4.off()

""" Switches between lights after initializing. """
def toggleLights():
    for led in leds:
        led.toggle()

""" For when the button is not pressed! """
def turnOff():
    for led in leds:
        led.off()

""" music initialize """
def loadMusic():
    mixer.init()
    mixer.music.load('bluechristmas.mp3')

""" play music """
def play():
    mixer.music.play(-1)

""" Stop music """
def stop():
    mixer.music.stop()
    mixer.music.rewind()

""" Main method cause I felt like it """
def main():
    loadMusic()
    sleepTime = 0.75
    justPlayed = False
    while True:
        if button.is_pressed:
            if not mixer.music.get_busy():
                justPlayed = True
                play()
            lights()
            time.sleep(sleepTime)
            toggleLights()
            time.sleep(sleepTime)
        else:
            if justPlayed:
                stop()
                turnOff()
                justPlayed = False

main()

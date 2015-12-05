""" 
    Matan Uchen
    In my continous adventures with hardware and circuitry I decided to
    get in the Christmas spirit.  Button toggles christmas colored LEDs
    cause why not.

"""
from pygame import mixer
from gpiozero import LED, Button
import time

button = Button(7)

led1 = LED(2)
led2 = LED(3)
led3 = LED(4)
led4 = LED(17)

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

""" Main method cause I felt like it """
def main():
    loadMusic()
    while True:
        if button.is_pressed:
            play()
            lights()
            time.sleep(0.4)
            toggleLights()
            time.sleep(0.4)
        else:
            stop()
            turnOff()

main()

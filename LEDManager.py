import datetime
import getopt
import sys
import time
import board
import neopixel
import threading


class KeyboardThread(threading.Thread):

    def __init__(self, input_cbk=None, name='keyboard-input-thread'):
        self.input_cbk = input_cbk
        super(KeyboardThread, self).__init__(name=name)
        self.start()

    def run(self):
        while True:
            self.input_cbk(input())  # waits to get input + Return


state = "default"

def my_callback(inp):
    # evaluate the keyboard input
    global state
    if inp in ("r", "red", "red night"):
        state = "red"
        print("State changed to", state)
    elif inp in ("w", "white", "white night"):
        state = "white"
        print("State changed to", state)
    elif inp in ("n", "none", "reset", "dark night", "dark", "out", "default"):
        state = "default"
        print("State changed to", state)
    else:
        print("State unchanged")
    refresh_state()


# start the Keyboard thread
kthread = KeyboardThread(my_callback)

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 267

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRBW

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)


def white():
    pixels.fill((0, 0, 0, 255))
    pixels.show()

def red():
    pixels.fill((255, 0, 0, 0))
    pixels.show()

def none():
    pixels.fill((0, 0, 0, 0))
    pixels.show()

def refresh_state():
    print(datetime.datetime.now(), "state is", state)
    if (datetime.datetime.now().hour >= 7 and datetime.datetime.now().hour <= 20) or state == "white":
        white()
    elif state == "red":
        red()
    else:
        none()

while True:
    refresh_state()
    time.sleep(10)

import datetime
import getopt
import sys
import time
import board
import neopixel

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


def main(argv):
    r = False
    try:
        opts, args = getopt.getopt(argv, "r", ["red="])
    except getopt.GetoptError:
        print('LEDManager.py (-r)')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("--red", "-r"):
            r = True
    while True:
        print(datetime.datetime.now())
        if datetime.datetime.now().hour >= 7 and datetime.datetime.now().hour <= 20:
            white()
        elif r:
            red()
        else:
            none()
        time.sleep(10)


if __name__ == "__main__":
    main(sys.argv[1:])
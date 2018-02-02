import time
import RPi.GPIO as GPIO
import sys
import random
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

PIXEL_COUNT = 32
 
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

def led_on(pos_start, pos_end):
    for i in range(pos_start, pos_end):
        pixels.set_pixel_rgb(i, 255, 255, 255)
        pixels.show()
        #pixels.set_pixel(pos, Adafruit_WS2801.RGB_to_color( 255,255,255 ))
        #pixels.show()

def led_off(pos_start, pos_end):
    for i in range(pos_start, pos_end):
        pixels.set_pixel_rgb(i, 0, 0, 0)
        pixels.show()

def led_alloff():
    for i in range(0, PIXEL_COUNT):
        pixels.set_pixel_rgb(i, 255, 255, 255)
        pixels.show()

def led_allon():
    for i in range(0, PIXEL_COUNT):
        pixels.set_pixel_rgb(i, 255, 255, 255)
        pixels.show()

def led_nightmode():
    for i in range(0, PIXEL_COUNT):
        pixels.set_pixel_rgb(random.random(), 255, 255, 255)
        pixels.show()

if __name__ == "__main__":
    # Clear all the pixels to turn them off.
    #pixels.clear() # alles auf weiss bzw. aus
    #pixels.show()  # Make sure to call show() after changing any pixels!

    if sys.argv[1] == 'led_on':
        led_on(int(sys.argv[2]), int(sys.argv[3])

    if sys.argv[1] == 'led_off':
        led_ff(int(sys.argv[2]), int(sys.argv[3])

    if sys.argv[1] == 'led_alloff':
        led_alloff()

    if sys.argv[1] == 'led_allon':
        led_allon()

    if sys.argv[1] == 'led_nightmode':
        led_nightmode()
 
import random
from machine import Pin, I2C, SPI
import st7789
import utime

import bme280

import vga1_bold_16x16 as font
import vga1_bold_16x32 as font2

i2c = I2C(1, freq=399361, scl=Pin(7), sda=Pin(6))
bme = bme280.BME280(i2c=i2c, address=0x76)

def main():
    spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
    tft = st7789.ST7789(
        spi,
        135,
        240,
        reset=Pin(12, Pin.OUT),
        cs=Pin(9, Pin.OUT),
        dc=Pin(8, Pin.OUT),
        backlight=Pin(13, Pin.OUT),
        rotation=1)

    tft.init()
    utime.sleep(0.5)
    
    tft.text(font,"PICO SENSE HAT", 0,0, st7789.RED)
    #tft.rect(100, 100, 100, 10, st7789.RED)
    tft.fill_rect(0, 20, 230,5, st7789.RED)
    
    utime.sleep(0.5)
    
    '''tft.fill(0)
    tft.text(font,"PICO SENSE HAT", 0,0, st7789.BLUE)
    #tft.rect(100, 100, 100, 10, st7789.RED)
    tft.fill_rect(0, 20, 230,5, st7789.RED)'''
    
    
    tft.fill_rect(100, 45, 5,65, st7789.CYAN)
    tft.text(font2,"BME280", 0,60, st7789.YELLOW)
    
    tft.fill_rect(100, 75, 15,5, st7789.CYAN)
    tft.fill_rect(100, 45, 15,5, st7789.CYAN)
    tft.fill_rect(100, 105, 15,5, st7789.CYAN)
    
    while 1:
        print("Temp: {temp} Pressure: {pre} Hum: {hum}".format(temp=bme.values[0],pre=bme.values[1],hum=bme.values[2]))
        tft.text(font,bme.values[0], 120,40, st7789.BLUE)
        tft.text(font,bme.values[1], 120,70, st7789.BLUE)
        tft.text(font,bme.values[2], 120,100, st7789.BLUE)
        utime.sleep(1)   
    
main()

import time,utime
from machine import I2C, Pin, SPI
from sgp40 import SGP40
import bme280
import tcs34725
import sht31
import Lcd1_14driver#lcd driver

LCD = Lcd1_14driver.Lcd1_14()
LCD.fill(LCD.white) 


i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=40000)#all sensor connected through I2C

rst = machine.Pin(3, machine.Pin.OUT)#GPIO 3(OUTPUT) pin to enable address of temperature and humidity sht21 sensor
rst.value(1)#high GPIO 3 pin to enable address of temperature and humidity sht21 sensor

bme = bme280.BME280(i2c=i2c) #pressure,temperature and humidity sensor
color = tcs34725.TCS34725(i2c)#color sensor
air_quality = SGP40(i2c, 0x59)#air quality sensor
temp_hum = sht31.SHT31(i2c, addr=0x45)#temperature and humidity

def info():     
    LCD.text("SB-COMPONENTS PICO SENSE HAT",5,5,LCD.red)
    LCD.text("SENSOR READING",70,25,LCD.red)
    LCD.text("PRESSURE    : ",10,50,LCD.red)
    LCD.text("TEMPERATURE :",10,65,LCD.red)
    LCD.text("HUMIDITY    :  ",10,80,LCD.red)
    LCD.text("AIR QUALITY :",10,95,LCD.red)
    LCD.text("COLOR       :",10,110,LCD.red)
    
while True:
    #temp,hum,press = bme.temperature,bme.humidity,bme.pressure
    info()
    pressure = bme.pressure
    Temp_Humid = temp_hum.get_temp_humi()
    Temp_Humid = list(Temp_Humid)
    Air_quality = air_quality.measure_raw()
    Color = color.read('rgb')
    
    temperature = "{0}{1:.2f}C".format("", Temp_Humid[0])
    humidity = "{0}{1:.2f}%".format("", Temp_Humid[1])
    
    print("Prssure  ",pressure)
    print("Temperature = ",temperature)
    print("humidity = ",humidity)
    print("Air quality = ",Air_quality)
    print("Color = ",Color)#R,G,B,C
    
    LCD.text(pressure, 120,50,LCD.blue)# print on tft screen
    LCD.text(str(temperature), 120,65,LCD.blue)# print on tft screen
    LCD.text(str(humidity), 120,80,LCD.blue)# print on tft screen
    LCD.text(str(Air_quality), 120,95,LCD.blue)# print on tft screen
    LCD.text(str(Color), 120,110,LCD.blue)# print on tft screen
    LCD.lcd_show()
    
    time.sleep(0.2)
    
    LCD.text(pressure, 120,50,LCD.white)# print on tft screen
    LCD.text(str(temperature), 120,65,LCD.white)# print on tft screen
    LCD.text(str(humidity), 120,80,LCD.white)# print on tft screen
    LCD.text(str(Air_quality), 120,95,LCD.white)# print on tft screen
    LCD.text(str(Color), 120,110,LCD.white)# print on tft screen
    



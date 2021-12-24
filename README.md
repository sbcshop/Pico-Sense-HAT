# Pico-Sense-HAT



## About the product
* <b> Pico sense hat have four sensors and these sensors have definate addresses
  * <b> SGP40 Air quality sensor (addr=0x59)
  * <b> SHT31 Temperature and Humidity sensor (addr=0x45)
  * <b> BME280 Pressure sensor (0x76)
  * <b> TCS34725 Color sensor (addr=0x29)
 
 
## Files in the folder
### In folder you see 6 files (except reabme.md file)
* <b>There are 5 libraries in this folder you need to save these libraries in the raspberry pi pico,
     4 libraries of sensors and 1 library of lcd display
  * <b> sgp40.py 
  * <b> sht31.py
  * <b> bme280.py
  * <b> tcs34725.py
  * <b> Lcd1_14driver.py
 
* <b> One file is there in the folder which run the main code (this code display the sensor reading),
      this code import all the libraries of sensors and lcd display,
   * <b> pico_sense_hat.py
 
 
 
## For setup the Board in thonny </b>
* Now connect USB Cable on USB Port of Pico.
* Open Thonny IDE and Choose interpreter as MicroPython (Raspberry Pi pico).

<img src="https://github.com/sbcshop/Raspberry-Pi-Pico-RFID-Expansion/blob/main/images/thonny-interpreter.PNG" />
 
 
 
 ####Now save the all the libraries inside the raspberry pi pico and rename the pico_sense_hat.py to main.py and save this also inside pico. 
     (main.py code automatically run when pico power on)


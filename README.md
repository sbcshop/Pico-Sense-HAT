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
* Now connect USB Cable on USB Port of Pico 1.
* Open Thonny IDE and Choose interpreter as MicroPython (Raspberry Pi pico).

<img src="https://github.com/sbcshop/Raspberry-Pi-Pico-RFID-Expansion/blob/main/images/thonny-interpreter.PNG" />

* Now Create a file "Lcd1_14driver.py" as same content from PICO LORA Expansion's github repository in thonny ide, and save it in root location of first Raspberry Pi Pico with same name "Lcd1_14driver.py" (without quotes).
* we have two codes "tx_rx_lora1.py" and "tx_rx_lora2.py" both the codes are same, only change in "txdata", in one of the code "txdata = 123456" and in other code "txdata = abcdef",from this we can see the message send or receive clearly in both the pi lora hat.
* Copy and Paste or Open the "tx_rx_lora1.py" code in thonny ide..
* Click on green play button to run example of Pico LORA Expansion on Board 1, You can either save this file on root location of PICO or on your Computer drive.


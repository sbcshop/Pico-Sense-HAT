## Pico Sense HAT Run via ST7789 lcd driver

## Uploading the ST7789 Python Firmware (we already update in this repository)
 * The firmware includes frozen python font files and pre-compiled objects with the st7789 C driver for a variety of devices.
 * The driver's library is provided as a single firmware.uf2 file, which is accessible here:
    https://github.com/russhughes/st7789_mpy/tree/master/firmware/RP2
    
 * Holding down the Pico's BOTSEL button while dragging this file into the mounted RP2 folder will allow you to load it.

## <b>There are 4 libraries(sensors library) in this folder you need to save these libraries in the raspberry pi pico,
  * <b> sgp40.py 
  * <b> sht31.py
  * <b> bme280.py
  * <b> tcs34725.py

## Run this file "pico_sense_hat_st7789.py"

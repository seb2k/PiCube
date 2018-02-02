#!/usr/bin/python

import socket
import fcntl
import struct
from time import *
from datetime import datetime
from i2clibraries import i2c_lcd_smbus
import os
#os.system("pkill -9 python");

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

lcd = i2c_lcd_smbus.i2c_lcd(0x27,1, 2, 1, 0, 4, 5, 6, 7, 3)

lcd.command(lcd.CMD_Display_Control | lcd.OPT_Enable_Display)
lcd.backLightOn()
lcd.clear()
dt = "{:%D}".format(datetime.now())
t = "{:%H:%M:%S}".format(datetime.now())

lcd.writeString( "Loading ." )
sleep(1)
lcd.writeString( "." )
sleep(1)
lcd.writeString( "." )
sleep(1)
lcd.writeString( "." )
sleep(1)
lcd.writeString( "." )
sleep(1)
lcd.clear()
lcd.writeString( "  I am PiCube!" )
sleep(8)
lcd.clear()

while True:
    lcd.writeString( "Time: " + t )
    lcd.setPosition( 2, 0 )
    lcd.writeString( "Date: " + dt )
    sleep(5)
    lcd.clear()
    lcd.writeString( "e0 " )
    lcd.writeString( get_ip_address('eth0' ) )
    lcd.setPosition( 2, 0 )
    lcd.writeString( "e1 " )
    lcd.writeString( get_ip_address('eth0:1' ) )
    sleep(5)
    lcd.clear()
    lcd.writeString( "w0 " )
    lcd.writeString( get_ip_address('wlan0' ) )
    lcd.setPosition( 2, 0 )
    lcd.writeString( "hn " + socket.gethostname() )
    sleep(5)
    lcd.clear()

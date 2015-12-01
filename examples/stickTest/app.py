#!/usr/bin/python
from sense_hat import SenseHat
import os
import time
from select import select
from evdev import InputDevice, list_devices, ecodes, categorize

#Create SenseHat object instance
sense = SenseHat()
#Create holding variable for the joystick input object instane
joystick = None
#Variable to break running loop.
running = True
#Configure Sense HAT display rotation
sense.set_rotation(0)
#Set Sense HAT display speed interval
scrollSpeed = 0.08

#Find the joystick input
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
    print(dev.phys)
    if dev.phys == "rpi-sense-joy/input0":
        joystick = dev

#Display temp reading in red
def display_temp():
    sense.show_message("{:.1f}".format(sense.temp) + "C", text_colour=[255, 0, 0], scroll_speed=scrollSpeed)

#Display temp reading from alt sensor in yellow
def display_temp_from_humidity():
    temp = sense.get_temperature_from_pressure()
    sense.show_message("{:.1f}".format(temp) + "C", text_colour=[255, 255, 0], scroll_speed=scrollSpeed)

#Display hunidity in green
def display_humidity():
    sense.show_message("{:.2f}".format(sense.humidity) + "%", text_colour=[0, 255, 0], scroll_speed=scrollSpeed)

#Display pressure in blue
def display_pressure():
    sense.show_message(("{:.2f}".format(sense.pressure)) + "mBar", text_colour=[0, 0, 255], scroll_speed=scrollSpeed)

while running:
    #Capture joystick events
    r, w, x = select([joystick.fd], [], [])
    for event in joystick.read():
        if event.type == ecodes.EV_KEY:
            #Print debug for joystick events
            print(categorize(event))
            #On press down exit program
            if event.code == 28 and event.value == 0:
                running = False

            #On up
            if event.code == 103 and event.value == 0:
                display_temp()

            #On right
            if event.code == 106 and event.value == 0:
                display_humidity()

            #On left
            if event.code == 105 and event.value == 0:
                display_pressure()

            #On down
            if event.code == 108 and event.value == 0:
                display_temp_from_humidity()

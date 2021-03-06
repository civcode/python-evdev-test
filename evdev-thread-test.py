from evdev import InputDevice, categorize, ecodes
import threading
import time
import os
import sys

status = 0
is_running = True
device_path = '/dev/input/event5'

if not os.path.exists(device_path):
    print('device {} not found'.format(device_path))
    sys.exit()

input = InputDevice(device_path)
print(input)

def getEvents():
    global status
    global is_running
    while is_running:
        event = input.read_one()
        if event:
            if event.code == ecodes.KEY_VOLUMEUP and event.value == 1:        
                #print("AB Shutter3 was pressed.\n")
                status = 1
            if event.code == ecodes.KEY_VOLUMEUP and event.value == 2:        
                #print("AB Shutter3 was released.\n")
                status = 2
        time.sleep(0.01)

t = threading.Thread(target=getEvents)
t.start()

try:
    while True:
        if status == 1:
            print("got status 1")
            status = 0
except KeyboardInterrupt:
    #print("exiting")
    is_running = False
    t.join()

from evdev import InputDevice, categorize, ecodes
import threading

status = 0
is_running = True

input = InputDevice('/dev/input/event5')
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

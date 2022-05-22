from evdev import InputDevice, categorize, ecodes

input = InputDevice('/dev/input/event5')

#prints out device info at start
print(input)
#print(gamepad.capabilities(verbose=True))

#evdev takes care of polling the controller in a loop
for event in input.read_loop():
    #print("event = {}, type = {}, value = {}".format(event.code, event.type, event.value))
    #print(categorize(event),"\n")
    if event.code == ecodes.KEY_VOLUMEUP and event.value == 1:        
        print("AB Shutter3 was pressed.\n")
    if event.code == ecodes.KEY_VOLUMEUP and event.value == 2:        
        print("AB Shutter3 was released.\n")

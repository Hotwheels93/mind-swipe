from pynput.keyboard import Key, Controller
from mindwave.mindwave import Headset
import time

keyboard = Controller()
key = "Key.down"
headsetSerial = '/dev/tty.BrainLink_Pro-i'
print("Initing the mindwave device at /dev/tty.BrainLink_Pro-i")
headset = Headset(headsetSerial)
time.sleep(2)
print("Init successful, starting the Illithid loop")
print('Connected, waiting 10 seconds for data to start streaming')
time.sleep(10)

while True:
    print (f'Attention: {headset.attention}')
    if headset.attention > 70:
        print("NextTikTok")
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(2)


    time.sleep(1)

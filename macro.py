import keyboard
from time import sleep
keyboard.wait("Shift")
for i in range(100):
    keyboard.press("Shift")
    keyboard.write('rock \n')
    sleep(1)
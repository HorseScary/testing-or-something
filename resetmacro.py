import pyautogui
import keyboard
from time import sleep

while True:
    keyboard.wait("Del")
    sleep(.1)
    pyautogui.press("esc")
    sleep(.1)
    pyautogui.click(x = 1000, y=700)
    sleep(2)
    pyautogui.click(x = 1000, y = 500)
    sleep(.1)
    pyautogui.click(x = 1500, y = 900)
    sleep(.1)
    pyautogui.click(x = 1500, y = 450, clicks= 3, interval= .1)
    sleep(.1)
    pyautogui.click(x = 500, y = 1000)


# 1000, 700
# 1000, 500
# 1500, 900

# 1500, 450
# 1000, 900
# 500, 1000
# pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
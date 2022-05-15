import pyautogui
import time as t
from PIL import ImageGrab
import keyboard
from datetime import datetime

time = 0


# if a fish is found -> press rightclick and give back 1
# else -> fishstate -1, give fish_state back, release rightclick if fish_state is 0
def is_fish(fish_state):
    global time, screenx, screeny
    im = ImageGrab.grab(bbox=(round(0.39583*screenx), round(0.78704*screeny)-1, round(0.55208*screenx), round(0.78704*screeny)+2))  # where to search for the fishs eye (it is easier to find than the whole fish)
    for pixel in im.getdata():  # looking for the colors of the fishs eye in the image (color changes if the fish pulls, so it won't recognise it then)
        if pixel == (242, 222, 61):
            fish_state = 1
            break
    if fish_state == 0: # stop to reel in
        pyautogui.mouseUp(button="right")
    elif fish_state == 1: # reel in
        pyautogui.mouseDown(button="right")
        time = datetime.now().timestamp()


# gives back if the colors of the caught message were found
def caught():
    global screenx,screeny
    im = ImageGrab.grab(bbox=(round(0.02865*screenx)-1, round(0.84907*screeny)-1, round(0.02865*screenx)+2, round(0.84907*screeny)+2))  # where to look for the caught message
    for pixel in im.getdata():
        if pixel in [(173, 173, 173),(255, 255, 255), (56, 197, 79), (50, 138, 255), (205, 59, 189)]:  # colors for treasure, common, uncommon, rare and epic fish
            return True
    return False



if __name__ == '__main__':
    while 1: # loop waiting for the bot so start
        if keyboard.is_pressed('shift'):
            break
        t.sleep(4)

    time = datetime.now().timestamp() + 4

    # throw out first time
    pyautogui.mouseDown(button="right")
    pyautogui.mouseUp(button="right")
    screenx = pyautogui.getActiveWindow().width
    screeny = pyautogui.getActiveWindow().height


    #----------------------------- bot-loop --------------------------------------
    while 1:
        fst = 0
        
        # reel in
        if datetime.now().timestamp() - time >= 11:
            pyautogui.mouseDown(button="right")
            pyautogui.mouseUp(button="right")
            pyautogui.mouseDown(button="right")
            pyautogui.mouseUp(button="right")
            time = datetime.now().timestamp()

        # does the minigame
        fst =  is_fish(fst)

        # throw
        if caught():
            pyautogui.mouseDown(button="right")
            pyautogui.mouseUp(button="right")
            time = datetime.now().timestamp()
            t.sleep(4)  # sleep until the caught message disappears

        # UI
        if keyboard.is_pressed('x'):
            break
        elif keyboard.is_pressed('p'):
            while 1:
                if keyboard.is_pressed('shift'):
                    time = datetime.now().timestamp()
                    pyautogui.mouseDown(button="right")
                    pyautogui.mouseUp(button="right")
                    break
                t.sleep(4)
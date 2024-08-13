import pyautogui
import random
import threading


def autoMove():
    threading.Timer(100, autoMove).start()
    pyautogui.click(100, 50)

  
    random_scroll = random.randint(-1000, +1000)
    x_axis = random.randint(100,1920)
    y_axis = random.randint(100,1080)


    pyautogui.moveTo(x_axis, y_axis, duration = 2)
    pyautogui.moveRel(0, 50, duration = 2)
    pyautogui.scroll(random_scroll)

    print(pyautogui.position())


    pyautogui.hotkey('ctrl', 'shift', 'tab')



autoMove()


#   pyautogui.moveTo(100, 100, duration = 2)

# while(True):
#         random_scroll = random.randint(-1000, +1000)
#         x_axis = random.randint(100,1920)
#         y_axis = random.randint(100,1080)


#         pyautogui.moveTo(x_axis, y_axis, duration = 2)
#         pyautogui.moveRel(0, 50, duration = 2)
#         pyautogui.scroll(random_scroll)

#         print(pyautogui.position())


#         pyautogui.hotkey('ctrl', 'shift', 'tab')

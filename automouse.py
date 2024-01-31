import pyautogui as pag
import time
import random
while True:
    x = random.randint(200, 1000)
    y = random.randint(200, 1000)
    pag.moveTo(x, y, duration=0.3)
    time.sleep(1)
    current_x, current_y = pag.position()
    if current_x != x or current_y != y:
        break
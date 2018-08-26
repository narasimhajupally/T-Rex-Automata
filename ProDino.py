import pyautogui
import time
import PIL.ImageGrab as ImageGrab
pyautogui.FAILSAFE = True

box_area1 = (530, 395, 595, 445) #box coordinates(x1,y1, x2,y2) to detect obstacles
pixel_plant1 = (12, 22) #pixel coordinates(x1,y1) of big plants
pixel_plant2 = (19, 29) #pixel coordinates(x1,y1) of small plants
pixel_plant3 = (17, 27) #pixel coordinates(x1,y1) of 3 in row plants
pixel_bird = (15, 7)

def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')
    print('Jump')

def duck():
    pyautogui.keyDown('down')
    time.sleep(0.05)
    pyautogui.keyUp('down')
    print('Duck')

play = True
while play:
    try:
        box = ImageGrab.grab(box_area1)
        p1 = box.getpixel(pixel_plant1)
        p2 = box.getpixel(pixel_plant2)
        p3 = box.getpixel(pixel_plant3)
        p4 = box.getpixel(pixel_bird)
        if p1 == (83, 83, 83) or p2 == (83, 83, 83) or p3 == (83, 83, 83):
            jump()
            time.sleep(0.06)
        #elif p4 == (83, 83, 83):
            #duck()
            #time.sleep(0.06)
    except Exception as e:
        play = False
        print(e)


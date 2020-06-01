import pyautogui
import time
from PIL import ImageGrab,ImageOps
import numpy

class Cordinates():
    replayBtn=(480,503)
    dinosaur=(207,534)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)
    pyautogui.keyDown('down')

def pressSapce():
    #pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.1)
    print("jump")
    #time.sleep(0.18 )
    pyautogui.keyUp('space')
    #pyautogui.keyDown ('down')

def imageGrab():
    #box = (Cordinates.dinosaur[0]+90,Cordinates.dinosaur[1],Cordinates.dinosaur[0]+150,Cordinates.dinosaur[1]+5)
    box = (214,492,381,505)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a=numpy.array(grayImage.getcolors())
    print(a.sum())
    return(a.sum())

#imageGrab()
# restartGame()
def main():
    #imageGrab()
    #restartGame()
    while True:
        if(imageGrab()!=2418) :
            pressSapce()
            time.sleep(0.1)

main()
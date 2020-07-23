import pyautogui as py
from PIL import Image,ImageGrab
import time

def hit(key):
    py.press(key)
    return


def iscollide(data):
    for i in range(400,700):
        for j in range(440,530):
            if data[i,j] < 100:
                hit("up")
                return
    
    # for i in range(400,700):
    #     for j in range(320,450):
    #         if data[i,j] < 100:
    #             hit("down")
    #             return
    return

if __name__ == "__main__":
    time.sleep(2)

    
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        iscollide(data)

        # # for cactus
        # for i in range(400,700):
        #     for j in range(440,530):
        #         data[i,j]=0

        # # for birds
        # for i in range(400,700):
        #     for j in range(320,450):
        #         data[i,j]=170

        image.show()
        break

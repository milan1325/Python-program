from pygame import mixer
import datetime
from time import time


def musiconloop(file,sttoper):
    mixer.init()
    mixer.music.load(file)
    while True:
        mixer.music.play()
        user_input = input("")
        if user_input == sttoper:
            mixer.music.stop()
            break

def logs(msg):
    with open("logs.txt","a") as f:
        f.write(f"{msg} {datetime.datetime.now()}\n")


if __name__ == "__main__":
    # musiconloop("water.mp3","drank")
    a = print("You want to exit this program then press 'q' ")
    init_water = time()
    init_eye = time()
    init_exercise = time()

    water_secs = 5
    eye_secs = 10
    exercise_secs = 20


    while True:
        if time() - init_water > water_secs:
            print("water drinking time. Enter 'drank' to stop the alarm")
            musiconloop("water.mp3","drank")
            init_water = time()
            logs("Drank water at ")

        if time() - init_eye > eye_secs:
            print("eyes exercise time. Enter 'done' to stop the alarm")
            musiconloop("eye.mp3","done")
            init_eye = time()
            logs("eyes relexed at ")

        if time() - init_exercise > exercise_secs:
            print("physical exercise time. Enter 'phy' to stop the alarm")
            musiconloop("physical.mp3","phy")
            init_exercise = time()
            logs("physical exercise at ")
        
        
    
from threading import Thread

import os

def play_sound(): 
    # import your script A
    os.system('python wren_roboto.py')

def CV2_stuff():
    # import your script B
    os.system('python main.py')
def kloaku():
    os.system('python kloaka_robot.py')


Thread(target = play_sound).start() 
Thread(target = CV2_stuff).start()
Thread(target = kloaku).start()

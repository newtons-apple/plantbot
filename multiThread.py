from threading import Thread
from playsound import playsound
import time
import move
move.setup()
def dance():
    for t in range(0,4,1):
        print('ab')
        time.sleep(0.5)
        print('bc')
        time.sleep(0.5)
        move.move(100,'forward','forward')
        time.sleep(0.8)
        move.move(100,'backward','backward')
        time.sleep(0.8)
        move.move(100,'forward','right',1)
        time.sleep(0.8)
        move.move(100,'forward','left',1)
        time.sleep(0.6)
def sing():
    playsound("christmas_song.wav")

if __name__ == "__main__":
    START, END = 0, 100000000
    result = list()
    th1 = Thread(target=dance)
    th2 = Thread(target=sing)
    
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    move.motorStop()

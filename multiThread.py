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
        time.sleep(1)
        move.move(100,'backward','backward')
        time.sleep(1)
        move.move(100,'forward','right',1)
        time.sleep(1)
        move.move(100,'forward','left',1)
        time.sleep(1)
def sing():
    playsound("christmas_song.wav")

if __name__ == "__main__":
    START, END = 0, 100000000
    result = list()
    th1 = Thread(target=dance, args=(1, START, END//2, result))
    th2 = Thread(target=sing, args=(2, END//2, END, result))
    
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    move.motorStop()

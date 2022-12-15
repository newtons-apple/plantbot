from multiprocessing import Process
from multiprocessing import freeze_support
from playsound import playsound
import time
import move

# move.setup()
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



if __name__=='__main__':
    freeze_support()
    # 프로세스를 생성합니다
    p1 = Process(target=dance) #함수 1을 위한 프로세스
    p2 = Process(target=sing) #함수 2을 위한 프로세스

    # start로 각 프로세스를 시작합니다. func1이 끝나지 않아도 func2가 실행됩니다.
    p1.start()
    p2.start()

    # join으로 각 프로세스가 종료되길 기다립니다 p1.join()이 끝난 후 p2.join()을 수행합니다
    p1.join()
    p2.join()
    move.motorStop()

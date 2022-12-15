import cv2
import numpy as np
import os
import speech_recognition as sr
from playsound import playsound
import time
import smbus
import time
import move
import ultrasonic
from multiprocessing import Process

move.setup()
I2C_CH = 1
BH1750_DEV_ADDR = 0x23

CONT_H_RES_MODE     = 0x10
CONT_H_RES_MODE2    = 0x11
CONT_L_RES_MODE     = 0x13
ONETIME_H_RES_MODE  = 0x20
ONETIME_H_RES_MODE2 = 0x21
ONETIME_L_RES_MODE  = 0x23
chunk = 1024

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> loze: id=1,  etc
# 이런식으로 사용자의 이름을 사용자 수만큼 추가해준다.
names = ['None', 'jiwon']

#우리가 사용할 표정 이미지 추가하기
happy= cv2.imread("happy.jpg",cv2.IMREAD_ANYCOLOR)
normal = cv2.imread("normal.jpg")
sad = cv2.imread("sad.jpg")

#이미지 띄울 창 만들기
cv2.namedWindow('face', cv2.WINDOW_NORMAL)
# cv2.setWindowProperty('face',cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow('face',normal)
cv2.waitKey(1000)
# Initialize and start realtime video capture
#window는 videoCapture(0) , linux는 videoCapture(-1)
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

#한바퀴 도는데 걸리는 시간
one_turn_time=15

#light sensor 
def readIlluminance():
    i2c = smbus.SMBus(I2C_CH)
    luxBytes = i2c.read_i2c_block_data(BH1750_DEV_ADDR, CONT_H_RES_MODE, 2)
    lux = int.from_bytes(luxBytes, byteorder='big')
    i2c.close()
    return lux

'''
 1초에 한번씩 돌면서 조도값 출력
'''
#lightcheck
def lightcheck():
    print('b-1')
    move.motorStop()
    time.sleep(1)
    move.move(100,'forward','right',1)
    start_time=time.time()
    while True:
        print('b-2')
        lux=readIlluminance()
        print(lux)
        if(lux>700):
            print('b-3')

            move.motorStop()
            time.sleep(1)
            break
        if(17<time.time()-start_time):
            print('b-4')

            break
        time.sleep(0.2)
    # start_time=time.time()
    # move.move(100,'forward','right',1)
    # print('b-2')
    # maxValue=[0,0]
    # while True:
    #     print('b-3')
    #     lux=readIlluminance()
    #     print(lux)
    #     if(lux>maxValue[0]):
    #         print('b-4')

    #         maxValue=[lux,time.time()]
    #     time.sleep(0.05)
    #     print('b-5')

    #     if(one_turn_time<time.time()-start_time):
    #         print('b-6')
    #         break
    # restart_time=time.time()
    # print('b-7')
    # while True:
    #     print('b-8')
    #     if(maxValue[1]-start_time<time.time()-restart_time):
    #         move.motorStop()
    #         print('b-9')
    #         break

#장애물 피하기
def avoidObstacle():
    print('avoid')
    move.move(100,'forward','left',1)
    time.sleep(4)
    move.motorStop()
    time.sleep(1)
    move.move(100,'forward','forward')
    time.sleep(4)
    move.motorStop()
    time.sleep(1)
    move.move(100,'forward','right',1)
    if(5>ultrasonic.checkdist()):
        avoidObstacle()
        return
    time.sleep(4)
    move.move(100,'forward','forward')
    time.sleep(4)
#춤추기
def dance():
    for t in range(0,7,1):
        move.move(100,'forward','forward')
        time.sleep(0.5)
        move.move(100,'backward','backward')
        time.sleep(0.5)
        move.move(100,'forward','right',1)
        time.sleep(0.5)
        move.move(100,'forward','left',1)
        time.sleep(0.5)
def sing():
    playsound("christmas_song.wav")

if __name__=='__main__':
    master = False
    while True:
        ret, img =cam.read()
        img = cv2.flip(img, 1)
        img = cv2.flip(img, -1)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )
        for(x,y,w,h) in faces:
            # cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                id = names[id]
                # confidence = "  {0}%".format(round(100 - confidence))
                cv2.imshow('face',happy)
                cv2.waitKey(10)
                playsound("hello.wav")
                time.sleep(1)
                cv2.imshow('face',normal)
                cv2.waitKey(10)
                master = True
                break

                

            else:
                id = "unknown"
                # confidence = "  {0}%".format(round(100 - confidence))
            
            # cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            # cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        # cv2.imshow('camera',img) 
        if master:
            master=False
            break



        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source,10,5)
            try:
                result = r.recognize_google(audio)
                if(result == "Merry Christmas"):
                    cv2.imshow('face',happy)
                    cv2.waitKey(10)
                    # sing()
                    # time.sleep(0.5)
                    p_a=Process(target=dance)
                    p_b=Process(target=sing)
                    p_a.start()
                    p_b.start()
                    p_a.join()
                    p_b.join()
                if(result == "are you having enough light"):
                    cv2.imshow('face',sad)
                    cv2.waitKey(10)
                    playsound("no.wav")
                    time.sleep(0.5)
                    while True:
                        print(1)
                        lightcheck()
                        print('a-1')
                        move.move(100,'forward','front')
                        time.sleep(8)
                        print('a-2')
                        lightcheck()
                        start_time=time.time()
                        pass2=False                 
                        while True:
                            move.move(100,'forward','front')
                            print(2)
                            #장애물 만나면
                            print(ultrasonic.checkdist())

                            if(5>ultrasonic.checkdist()):
                                print(3)
                                move.motorStop()
                                time.sleep(1)
                                avoidObstacle()
                                print('55')
                                pass2=True
                                break
                            if(20<(time.time()-start_time)):
                                print('44')
                                pass2=True
                                break
                        print('77')
                        if(pass2):
                            print('66')
                            break
                    move.move(100,'forward','forward')
                    while True:
                        print('last1')
                        lux = readIlluminance()
                        print(lux)
                        if(700< lux):
                            print(5)
                            move.motorStop()
                            break
                        time.sleep(0.2)
                    print(6)
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
        cv2.imshow('face',normal)
        cv2.waitKey(10)


    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")

    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Say something!")
    #     audio = r.listen(source)
    # r.recognize_google(audio)

    cam.release()
    cv2.destroyAllWindows()
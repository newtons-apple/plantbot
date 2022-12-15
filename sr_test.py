import speech_recognition as sr
import cv2
#우리가 사용할 표정 이미지 추가하기
happy= cv2.imread("happy.jpg",cv2.IMREAD_ANYCOLOR)
normal = cv2.imread("normal.jpg")
sad = cv2.imread("sad.jpg")
#이미지 띄울 창 만들기
cv2.namedWindow('face', cv2.WINDOW_NORMAL)
# cv2.setWindowProperty('face',cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow('face',normal)
cv2.waitKey(3000)

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source,10,5)
        print(audio)
        try:
            result = r.recognize_google(audio)
            if(result == "Merry Christmas"):
                cv2.imshow('face',happy)
                cv2.waitKey(10)
                # playsound("christmas_song.wav")
                # time.sleep(0.5)
            if(result == "lack of light"):
                cv2.imshow('face',sad)
                cv2.waitKey(10)
                # playsound("christmas_song.wav")
                # time.sleep(0.5)
                # while True:
                #     result=lightcheck()
                #     move.move(100,'forward','front')
                #     start_time=time.time()
                #     while (2<time.time()-start_time):
                #         #장애물 만나면
                #         if(5>ultrasonic.checkdist()):
                #             avoidObstacle()                  
                #     if(1000< readIlluminance()):
                #         break
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
    cv2.imshow('face',normal)
    cv2.waitKey(10)
import cv2
import time
#우리가 사용할 표정 이미지 추가하기
happy= cv2.imread("happy.jpg",cv2.IMREAD_ANYCOLOR)
normal = cv2.imread("normal.jpg")
a=normal
#이미지 띄울 창 만들기
cv2.namedWindow('face', cv2.WINDOW_NORMAL)
# cv2.setWindowProperty('face',cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# cv2.imshow('face',normal)
# cv2.imshow('face',normal)
# print('Enter your name:')
# x = input()
# cv2.waitKey(int(x))
# cv2.destroyAllWindows()
cv2.imshow('face',a)
cv2.waitKey(10)
cv2.imshow('face',happy)
cv2.waitKey(10)
time.sleep(5)
# while True:


#     # time.sleep(5)

#     print('Enter your name:')
#     x = input()

#     if(x=='1'):
#         a=happy
#     if(x=='2'):
#         a=normal
#     if(x=='3'):
#         cv2.destroyAllWindows()
#         break
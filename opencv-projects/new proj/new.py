import cv2 as cv
img=cv.imread('images/test.jpg')

# reading images:-
cv.imshow('test', img)

# reading videos:-
# capture=cv.VideoCapture('images/video.mp4')
# while True:
#     isTrue, frame= capture.read()
#     cv.imshow('test', frame)
#     # to stop the video:-
#     if cv.waitKey(20) & 0xFF==ord('q'):
#         break
# capture.release()
# cv.destroyAllWindows()


cv.waitKey(0)
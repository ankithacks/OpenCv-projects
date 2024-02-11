import cv2 as cv

img=cv.imread('images/test.jpg')
cv.imshow('Img' , img)

# resizing the images:-
def rescaleImg(frame, scale=0.75):
    # this will work for images, videos and live videos
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[1] * scale)
    dimensions=(width, height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

def changeRes(width , height):
    # only work for live videos
    capture.set(3, width)
    capture.set(4, height)


# reading videos:-
capture=cv.VideoCapture('images/video.mp4')
while True:
    isTrue, frame= capture.read()
    
    frame_resized= rescaleImg(frame, scale=.2)

    cv.imshow('test', frame)
    cv.imshow('video resized', frame_resized)

    # to stop the video:-
    if cv.waitKey(20) & 0xFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
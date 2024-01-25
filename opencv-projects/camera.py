import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    width=int(cap.get(3))   #it will give the width property of the frame
    height=int(cap.get(4))   #it will give the height property of the frame

    image=np.zeros(frame.shape, np.uint8)
    smaller_frame=cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
    image[:height//2, width//2:]= cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2]= smaller_frame
    image[:height//2, :width//2]= cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:]= smaller_frame
    
    
    # display the frame
    # cv2.imshow('frame', image)
    cv2.imshow('frame', frame)

    if(cv2.waitKey(1)==ord('q')):
        # this means that if we press q, it gets quitted with the ascii value after waiting for 1 millisecond and will only quit if we press q else it will go on till infinity
        break

cap.release()   #will release the camera
cv2.destroyAllWindows()
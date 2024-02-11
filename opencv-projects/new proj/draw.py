import cv2 as cv
import numpy as np


# creating a blank image and working over it:-
blank=np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)


# drawing over a given photo:-
# img=cv.imread('images/test.jpg')
# cv.imshow('test', img)

# paint the image a certainn colour:-
# blank[:]=0,0,255   #this will cover the whole scrren with red color
# blank[200:300, 300:400] =0,0, 255  #this will cover the screen with given pixel values
# cv.imshow('Green', blank)

# draw a rectaangle:-
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) #you can asign an interger value to have a thivh line and if you want to fill in the colour we specify it as:l- cv.FILLED in thickness
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

# draw a circle:-
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40 , (0,0,255), thickness=2 )
cv.imshow('Circle', blank)

# draw a line:-
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
cv.imshow('Line', blank)

cv.waitKey(0)
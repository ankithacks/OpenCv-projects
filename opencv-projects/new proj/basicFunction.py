import cv2 as cv

img=cv.imread('images/test.jpg')
cv.imshow('test', img)

# converting an image to graySCale that is coonverting the image to gray colour:-
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('test', gray)

# blur an image:-(the tuple inside the bracket has to be an odd number and to increase the blurr effeect we increase it based on odd number only)
blur=cv.GaussianBlur(img, (11,11), cv.BORDER_DEFAULT)
cv.imshow('BLur', blur)

# creating an edge cascade that is trying to find the image edges:-
canny=cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# dilating the images:-
dilated=cv.dilate(canny, (3,3), iterations=3)
cv.imshow('dilation', dilated)

# eroding the image:_
eroded=cv.erode(dilated, (3,3), iterations=3)
cv.imshow('eroded', eroded)

# resize and crop the images:-
resize=cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resize)

# cropping:-
crop=img[50:200, 200:400]
cv.imshow('Cropped', crop)

cv.waitKey(0)
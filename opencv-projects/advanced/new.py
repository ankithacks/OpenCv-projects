import cv2
img =cv2.imread('assets/logo.jpg', -1)
# 0,cv2.IMREAD_GRAYSCALE: loads image in grayscale mode
# -1, cv2.IMREAD_COLOR: loads a color image.
# 1, cv2.IMREAD_UNCHANGED: loads image as such including alpha channel

# resizing the image
img=cv2.resize(img, (400, 400))
# img=cv2.resize(img, (0,0), fx=2, fy=2)

# rotate the image
img=cv2.rotate(img, cv2.ROTATE_180)

# to save the image we do as:-
cv2.imwrite('new_img.jpg', img)

# display image
cv2.imshow('ImageTest',img)
# we write here 0 whixh means its infinite. If mentioned other stuffs like 1000 which means 1 second it will open up and then close instantly
cv2.waitKey(0)
cv2.destroyAllWindows()
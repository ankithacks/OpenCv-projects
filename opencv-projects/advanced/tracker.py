import cv2

cap=cv2.VideoCapture(0)
tracker=cv2.TrackerMIL_create()


success, img=cap.read()
box=cv2.selectROI("Tracking", img, False)
tracker.init(img, box)

def drawBox(img, box):
    x, y, w, h=int(box[0]),int(box[1]),int(box[2]),int(box[3])
    cv2.rectangle(img,(x,y), ((x+w),(y+h)), (255,0,255), 3, 1)
    cv2.putText(img,"Tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,255, 0), 2)


while True:
    timer=cv2.getTickCount()
    success, img=cap.read()

    success, box=tracker.update(img)
    if success:
        drawBox(img, box)
    else:
        cv2.putText(img,"lost", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,0,255), 2)

    fps=cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img,str(int(fps)), (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,0,255), 2)
    cv2.imshow("tracking", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
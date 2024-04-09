import cv2 as cv
import time
import mediapipe as mp

# cap = cv.VideoCapture(0)

class handDetect():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.mphands= mp.solutions.hands
        self.hands=self.mphands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils

    def findHands(self, img):
        imageRGB=cv.cvtColor(img, cv.COLOR_BGR2RGB)
        result=self.hands.process(imageRGB)
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                    h,w,c=img.shape
                    cx,cy=int(lm.x*w), int(lm.y*h)    
                    print(id, cx,cy)
                
                    if id==0:
                    # we are talking about the first landmark
                         cv.circle(img, (cx,cy), 30, (255,255,0), cv.FILLED)
                    self.mpDraw.draw_landmarks(img, handLms, self.mphands.HAND_CONNECTIONS)



# pTime=0
# cTime=0

# while True:
#     success, img = cap.read()
# imageRGB=cv.cvtColor(img, cv.COLOR_BGR2RGB)
# result=hands.process(imageRGB)
#     # print(result.multi_hand_landmarks)
# if result.multi_hand_landmarks:
#     for handLms in result.multi_hand_landmarks:
#         for id, lm in enumerate(handLms.landmark):
#                 # print(id, lm)
#             h,w,c=img.shape
#             cx,cy=int(lm.x*w), int(lm.y*h)    
#             print(id, cx,cy)
                
#             if id==0:
#                     # we are talking about the first landmark
#                 cv.circle(img, (cx,cy), 30, (255,255,0), cv.FILLED)
#             mpDraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS)

    # cTime=time.time()
    # fps=1/(cTime-pTime)
    # pTime=cTime

    # cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    # cv.imshow("image", img)
    # if cv.waitKey(1) & 0xFF == ord('q'):
    #     break

cap.release()
cv.destroyAllWindows()


def main():
    pTime=0
    cTime=0

    while True:
        success, img=cap.read()
        cap=cv.VideoCapture(0)
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime

        cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255,0, 255), 3)

        cv.imshow("image", img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

if __name__=="__main__":
    main()
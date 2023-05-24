import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random
cap=cv2.VideoCapture(0)
cap.set(3,640) #width400
cap.set(4,480) #height375

detector=HandDetector(maxHands=1)

timer=0
stateResults=False
startGame=False
scores=[0,0]

while True:
    imgBG=cv2.imread("resources/BG.png")
    success,img=cap.read()
    
    
    imgScaled=cv2.resize(img,(0,0),None,0.781,0.781)
    imgScaled=imgScaled[:,53:453]
    
    hands,img=detector.findHands(imgScaled)
    if startGame:
        if stateResults is False:
            timer=time.time()-intialTime
            cv2.putText(imgBG,str(int(timer)),(660,448),cv2.FONT_HERSHEY_PLAIN,3,(38,43,47),4)
            if timer>3:
                stateResults=True
                timer=0
                if hands:
                   playerMove=None 
                   hand=hands[0]
                   fingers=detector.fingersUp(hand)
                   if fingers==[0,0,0,0,0]:
                       playerMove=1
                   if fingers==[1,1,1,1,1]:
                       playerMove=2
                   if fingers==[0,1,1,0,0]:
                       playerMove=3
                   randomNumber=random.randint(1,3)
                   imgAI=cv2.imread(f'resources/{randomNumber}.png',cv2.IMREAD_UNCHANGED)
                   imgBG=cvzone.overlayPNG(imgBG,imgAI,(189,321))
                   
                   if(playerMove==1 and randomNumber==3) or\
                       (playerMove==2 and randomNumber==1) or\
                        (playerMove==3 and randomNumber==2):
                            scores[1]+=1
                    
                   if(playerMove==3 and randomNumber==1) or\
                       (playerMove==1 and randomNumber==2) or\
                        (playerMove==2 and randomNumber==3):
                            scores[0]+=1
                   
                   print(playerMove)
       
       
        
        
        
        
    imgBG[278:653,830:1230]=imgScaled
    
    if stateResults:
        imgBG=cvzone.overlayPNG(imgBG,imgAI,(189,321))
    
    cv2.putText(imgBG,str(scores[0]),(464,251),cv2.FONT_HERSHEY_PLAIN,3,(38,43,47),4)
    cv2.putText(imgBG,str(scores[1]),(1171,251),cv2.FONT_HERSHEY_PLAIN,3,(38,43,47),4)
    #cv2.imshow("Image",img)
    cv2.imshow("BG",imgBG)
    #cv2.imshow("Scaled",imgScaled)
    
    key=cv2.waitKey(1)
    if key==ord('d'):
        startGame =True
        intialTime=time.time()
        stateResults=False
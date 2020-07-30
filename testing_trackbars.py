import cv2
import numpy as np
import time

load_from_disk = True
 
if load_from_disk:
    penval = np.load('pen.npy')
 
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
 
kernel = np.ones((5,5),np.uint8)
 
while(1):
    ret, frame = cap.read()
    if not ret:
        break
         
    frame = cv2.flip( frame, 1 )

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
     
    if load_from_disk:
            lower_range = penval[0]
            upper_range = penval[1]
             
    else:
       lower_range  = np.array([26,80,147])
       upper_range = np.array([81,255,255])
     
    mask = cv2.inRange(hsv, lower_range, upper_range)
     
    mask = cv2.erode(mask,kernel,iterations = 1)
    mask = cv2.dilate(mask,kernel,iterations = 2)
 
    res = cv2.bitwise_and(frame,frame, mask= mask)
 
    mask_3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
     
    stacked = np.hstack((mask_3,frame,res))
    cv2.imshow('Trackbars',cv2.resize(stacked,None,fx=0.4,fy=0.4))
     
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
 
cv2.destroyAllWindows()
cap.release()
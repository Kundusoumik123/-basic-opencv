import cv2
#import numpy as np
#import os

cap=cv2.VideoCapture("../Videos/RoseBloom.mp4")


def partA():
    count=0
    success=True
    fps=int(cap.get(cv2.CAP_PROP_FPS))
    while success:
        success,image=cap.read()
        count+=1
        #print(count)
        if count==(fps*6):
             cv2.imwrite("../Generated/frame_as_6.jpg",image)

def partB():
    count1=0
    success1=True
    fps=int(cap.get(cv2.CAP_PROP_FPS))
    while success1:
        success1,image1=cap.read()
        count1+=1
        if count1==(fps*6):
             image1[:,:,0]=0
             image1[:,:,1]=0
             red_image=image1
             cv2.imshow("image",red_image)
             cv2.imwrite("../Generated/frame_as_6_red.jpg",image1)

partA()
partB()
cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2
import os

fpath = os.getcwd() + '\\images'
plist = [f for f in os.listdir(fpath) if os.path.isfile(os.path.join(fpath, f))]


def fadeIn (img1, img2, len=50): 
    for IN in range(0,len):
        fadein = IN/float(len)
        dst = cv2.addWeighted( img1, 1-fadein, img2, fadein, 0)
        cv2.imshow('window', dst)
        cv2.waitKey(1)
        #print(fadein)
    cv2.waitKey(0)

if(len(plist)>0):
    img1 = cv2.imread('images\\' + plist[0])
    cv2.imshow('window', img1)
    cv2.waitKey(0)


for i in range(1,len(plist)):
    img1 = cv2.imread('images\\' + plist[i-1])
    img2 = cv2.imread('images\\' + plist[i])
    fadeIn(img1,img2)

    

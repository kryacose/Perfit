import cv2
import numpy as np
import os
import math

input_dir = os.getcwd() + '\\images\\p1.jpg'
img = cv2.imread(input_dir)
rows = img.shape[0]
cols = img.shape[1]
cnum=0
xlist=[]
ylist=[]


#mouse callback function
def mark_point(event,x,y,flag,param):
    if(event == cv2.EVENT_LBUTTONDBLCLK):
        cv2.circle(img,(x,y), 2, (0,255,0), 2)
        xlist.append(x)
        ylist.append(y)
        cnum+=1
        print("CNUM: ",cnum,"   x,y: ",xlist[cnum-1],",",ylist[cnum-1])
        


def rot():
    print("Enter angle: ",end = ' ')
    x=int(input())
    M = cv2.getRotationMatrix2D((cols/2,rows/2),x,1)
    return cv2.warpAffine(img,M,(cols,rows))

def scale():
    print("Enter Scaling factor: ",end = ' ')
    x=float(input())
    return cv2.resize(img,(math.floor(x*cols), math.floor(x*rows)), interpolation = cv2.INTER_CUBIC)
    

def align():
    print("Mark 4 Points: ",end = ' ')

    global cnum
    global xlist
    global ylist
    cnum = 0
    xlist = []
    ylist = []
    

    
    cv2.imshow('image',img)
    cv2.waitKey(30000)
    

    print(xlist,ylist)

    pts1 = np.float32([[xlist[0],ylist[0]],[xlist[1],ylist[1]],[xlist[2],ylist[2]],[xlist[3],ylist[3]]])
    pts2 = np.float32([[0,0],[cols,0],[0,rows],[cols,rows]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    return cv2.warpPerspective(img,M,(cols,rows))
    
def display():
    cv2.imshow('image',img)
    cv2.waitKey(10000)

cv2.namedWindow('image')
cv2.setMouseCallback('image',mark_point)
c=1
while(True):
    print("1)Rotate   2)Scale   3)Align   4)Display")
    c=int(input())
    if(c==1):
        img=rot()
        display()
    elif(c==2):
        img = scale()
        rows = img.shape[0]
        cols = img.shape[1]
        display()
    elif(c==3):
        img = align()
        display()
    elif(c==4):
        display()
    else:
        break

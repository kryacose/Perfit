import cv2 
import os
import numpy as np 

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (200,0,440,480)
cnum=0
xlist=[]
ylist=[]

def mark_point(event,x,y,flag,param):
    global cnum
    global xlist
    global ylist
    if(event == cv2.EVENT_LBUTTONDBLCLK and cnum<2):
        cv2.circle(img,(x,y), 2, (0,255,0), 2)
        xlist.append(x)
        ylist.append(y)
        cnum+=1
        print("CNUM: ",cnum,"   x,y: ",xlist[cnum-1],",",ylist[cnum-1])

def mask(img):
    mask = np.zeros(img.shape[:2],np.uint8)
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]
    return img

input_dir = os.getcwd() + '\\images\\Faces\\p5.jpg'


#make output folder if it doesnt exist

img = cv2.imread(input_dir)
cv2.namedWindow('image')
cv2.setMouseCallback('image',mark_point)

while(cnum<2):
    cv2.imshow('image',img)
    cv2.waitKey(10)
cv2.destroyAllWindows()

rect = (xlist[0],ylist[0],xlist[1]-xlist[0],ylist[1]-ylist[0])
# cv2.imshow('window', img)
# cv2.waitKey(0)
masked_img = mask(img)

cv2.imshow('image',masked_img)
cv2.waitKey(0)

    


import cv2
import numpy as np
import os


input_dir = os.getcwd() + '\\images\\Circle\\test.jpg'
img = cv2.imread(input_dir,0)
img = cv2.medianBlur(img,5)

cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=60,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    #size of circle
    print(str(i[2]))
    cv2.putText(img,str(i[2]),(i[0],i[1]), cv2.FONT_HERSHEY_SIMPLEX, 50,(0,0,255),10)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
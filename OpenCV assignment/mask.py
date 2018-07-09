import cv2 
import os
import numpy as np 

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (200,0,440,480)

def mask(img):
    mask = np.zeros(img.shape[:2],np.uint8)
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]
    return img

input_dir = os.getcwd() + '\\mask_in'
output_dir = os.getcwd() + '\\mask_out'

#make output folder if it doesnt exist
if not os.path.exists(output_dir):
  os.mkdir(output_dir)

#get list of input pictures
pic_list = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]


for i in range(len(pic_list)):
    img = cv2.imread(input_dir + '\\' + pic_list[i])
    # cv2.imshow('window', img)
    # cv2.waitKey(0)
    masked_img = mask(img)
    cv2.imwrite(output_dir + '\\' + str(i) + '.jpg' , masked_img )

    


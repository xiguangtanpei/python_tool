from __future__ import print_function 
from __future__ import division 
import os 
import cv2 as cv 
import numpy as np 
import sys 


# hdri 转灰度的测试 
# 后续的亮度比较会用到 这里是一个测试 


hdrpath = r"L:\Project\temp\quse\snowy_hillside_2k.hdr"

hdrdps   =  os.path.splitext(hdrpath)[0] +"_ps_" +  os.path.splitext(hdrpath)[1]     # ps 的去色九三 

hdrlum   =   os.path.splitext(hdrpath)[0] +"_lum_" +  os.path.splitext(hdrpath)[1]   # 亮度计算 

hdreys   =   os.path.splitext(hdrpath)[0] +"_eye_" +  os.path.splitext(hdrpath)[1]     #感知计算 


img = cv.imread(hdrpath ,flags = cv.IMREAD_ANYDEPTH) 

img_ps  =cv.imread(hdrdps ,flags = cv.IMREAD_ANYDEPTH) 
img_lum = cv.imread(hdrlum ,flags = cv.IMREAD_ANYDEPTH) 
img_eye = cv.imread(hdreys ,flags = cv.IMREAD_ANYDEPTH) 

key = [400 , 1229 ]

print ("打印默认的颜色情况：" ,  key )
print ( img[key[0] , key[1] ]  )

print("打印ps 的去色处理 " ,  key )
print ( img_ps[key[0] , key[1] ]  )

print("打印 lum 计算 " ,  key )
print ( img_lum[key[0] , key[1] ]  )

print("打印去色眼睛影响原色" ,  key)
print ( img_eye[key[0] , key[1] ]  )

from __future__ import print_function 
from __future__ import division 
import os 
import cv2 as cv 
import numpy as np 
import sys 


# hdri 转灰度的测试 
# 后续的亮度比较会用到 这里是一个测试 
# 这里是以后后续算法计算  




hdrpath = r"L:\Project\temp\reader_write_hdr\parched_canal_4k.hdr"

hdrdps   =  os.path.splitext(hdrpath)[0] +"_ps_" +  os.path.splitext(hdrpath)[1]     # ps 的去色九三 

hdrlum   =   os.path.splitext(hdrpath)[0] +"_lum_" +  os.path.splitext(hdrpath)[1]   # 亮度计算 

hdreys   =   os.path.splitext(hdrpath)[0] +"_eye_" +  os.path.splitext(hdrpath)[1]     #感知计算 


img = cv.imread(hdrpath ,flags = cv.IMREAD_ANYDEPTH) 

img_ps  = np.copy(img)
#img_lum = np.copy(img) 
#img_eye = np.copy(img) 
 


# 关于hdri 去色 比较研究 ，只要是用来比较图形亮度使用  

# ps现在的去色算法  
#http://hqok.net/article-843-1.html 
#  CNew = (Max(R,G,B) + Min(R,G,B)) / 2  hdr 去


#photometric/digital itu bt.709:

#y = 0.2126 r + 0.7152 g + 0.0722 b
#digital itu bt.601 (gives more weight to the r and b components):

#y = 0.299 r + 0.587 g + 0.114 b





totoinfo = img.shape 
pwidth = (totoinfo[1]-1 )
pheight= totoinfo[0]-1 



maxwidth  = 0 
maxheight = 0 
colorfloat = 0 
maxinforkey =[0,0]
singlecolor  = 0.0 

for i in range (0 ,pheight):
    for j in range(0,pwidth ):
       index = img[i , j ]  # 三色 

       # print(index )
       colortoto =  (max(index[0] ,index[1] ,index[2] ) +min (index[0] ,index[1] ,index[2]))/2.0 
       r = index[0] 
       g = index[1] 
       b = index[2] 


       # 计算的灰度 
       newscolor_ps   =    np.array([colortoto ,colortoto ,colortoto ]    )

       newcolor_lum =     0.2126*r + 0.7152*g + 0.0722*b
       newcolor_eye =     0.299*r + 0.587*g + 0.114*b       


       img_ps[i , j ]=  newscolor_ps 
       #img_lum [i , j ]=  newcolor_lum 
       #img_eye [i , j ]=  newcolor_eye    

                 
       #
    #if i == 30 :
    #    print ( type(singlecolor)) 
    #    print ( type(singlecolor)) 


cv.imwrite (hdrdps , img_ps)


#cv.imwrite (hdrlum , img_lum  )
#cv.imwrite (hdreys , img_eye  )

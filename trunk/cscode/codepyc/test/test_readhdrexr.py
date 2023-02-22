from __future__ import print_function 
from __future__ import division 
import os 
import cv2 as cv 
import numpy as np 
import sys 

hdrp = r"L:\Project\temp\4\TrueHDRI_190111EitaiBridgeA_L1000_SunOn_camera.hdr"
exrp = r"L:\Project\temp\4\TrueHDRI_190111EitaiBridgeA_L1000_SunOn_camera.exr"

# 获取最大亮度 

def  readcolor   (file  , zuobiao)  : 
    img = cv.imread(file ,flags = cv.IMREAD_UNCHANGED  ) 
    totoinfo = img.shape 
    pwidth = (totoinfo[1] )
    pheight= totoinfo[0]
    tem = None 
    temk = False                                       
    #for i in range (0 ,pheight):
    #    for j in range(0,pwidth ):
    #        if i == zuobiao[0] :
    #            if j == zuobiao[1]:
    #                    temk =True 
    #                    tem =img[i , j ]  # 三色 c
    #                    break 
    #    if temk ==True :
    #        break  

      
    color =  (img[zuobiao[1] ,zuobiao[0]])  
    return  ([color[2] ,color[1],color[0]])

def  read_bigvalue    (file  )  : 
    img = cv.imread(file ,flags = cv.IMREAD_UNCHANGED  ) 
    totoinfo = img.shape 
    pwidth = (totoinfo[1] )
    pheight= totoinfo[0]
    tem = None 
    temvalue = 0                               
    for i in range (0 ,pheight):
        for j in range(0,pwidth ):
                    tem =img[i , j ]  # 三色 c
                     
                    if  str(tem.max()) != "inf" : 
                        if temvalue < tem.max()    :
                              temvalue = tem.max()

    #color =  (img[zuobiao[1] ,zuobiao[0]])  
    #return  ([color[2] ,color[1],color[0]])
    return  temvalue 



if __name__ == "__main__"  :
    print (read_bigvalue (hdrp ))
    print (read_bigvalue (exrp ))
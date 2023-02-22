from __future__ import print_function 
from __future__ import division 
import os 
import cv2 as cv 
import numpy as np 
import sys 
import math 


# 注意专门针对 16位数据 进行半精度处理 



def  readcolor   (file  , zuobiao)  : 
    img = cv.imread(file ,flags = cv.IMREAD_UNCHANGED  ) 
    totoinfo = img.shape 
    pwidth = (totoinfo[1] )
    pheight= totoinfo[0] 
    tem = None 
    temk = False   
    # 计算平均 

    
    #for i in range (0 ,pheight):
    #    for j in range(0,pwidth ):
    #        if i == zuobiao[0] :
    #            if j == zuobiao[1]:
    #                    temk =True 
    #                    tem =img[i , j ]  # 三色 c
    #                    break 
    #    if temk ==True :
    #        break 
    #        数据的数据是 gbr  需要除以2 并向上取整 


    color =   (img[zuobiao[1] ,zuobiao[0]])
    newcolor = [ math.ceil (color[2]/2. )/32768.0 ,math.ceil( (color[1]/2.))/32768.0  , math.ceil ((color[0]/2.))/32768.0]            
    return  newcolor

# y用来计算平均 
def calca_pj   (file ) :
    img = cv.imread(file ,flags = cv.IMREAD_UNCHANGED  ) 
    totoinfo = img.shape 
    pwidth = (totoinfo[1] )
    pheight= totoinfo[0] 
    tem = None 
    temk = False   
    # 计算平均 

    temp = np.array([0.0,0.0,0.0] ,dtype ="float64") 
    for i in range (0 ,pheight):
        for j in range(0,pwidth ):
            t =img[i , j ]  # 三色 c
                     
            temp+=t
            #print (temp)
    # 全部加在除以 
    num= pheight * pwidth  

    color =  temp / num 
    newcolor = [ math.ceil (color[2]/2. )/32768.0 ,math.ceil( (color[1]/2.))/32768.0  , math.ceil ((color[0]/2.))/32768.0]  
    return  (newcolor)
    



                        

if __name__ == "__main__" :
    import cls.get_hdri_lum as lum 
    tiff= r"C:\tmp\te\converted\IMG_3697_one.tif"
    tiffcopy = r"C:\tmp\te\converted\IMG_3697.tif"
   


    #small_tif =  r"C:\tmp\read_tiff\small_tif.tif"
    #print(calca_pj (tiff)  )
    #print (calca_pj (tiffcopy))

    #对于


    # ##对于点比较 
    #key = [2786 ,2249] 
    #onecolor =  ( readcolor (tiff ,key))
    #twocolor  =  ( readcolor (tiffcopy ,key))

    #o  = lum.get_hdri_lum().hdri_lum(onecolor)
    #o1  = lum.get_hdri_lum().hdri_lum(twocolor)
    #print("以下是没有处理白平衡之前的亮度") 
    #print (o)

    #print ("以下是处理白平衡之后的亮度") 
    #print (o1 )

    


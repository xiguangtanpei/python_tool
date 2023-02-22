from __future__ import print_function 
from __future__ import division 
import os 
import cv2 as cv 
import numpy as np 

#https://matiascodesal.com/blog/how-read-hdr-image-using-python/ 

hdrpath = r"L:\Project\temp\reader_write_hdr\TrueHDRI_190111EitaiBridgeA_L1000_SunOff_camera_256.hdr"

img = cv.imread(hdrpath ,flags = cv.IMREAD_ANYDEPTH) 





#print(img)
# 获取最大亮度  
#mm= img.max()
#print("获取hdr图最大亮度")
#print (mm)  


# 数组中的元素，之类其实获取的是颜色 我知道 图形大小是 256*128 *3 
#print ("获取数组的总数量") 
#print (img.shape  )





# 转成list 
#print ( "获取 高度 宽度 ")
totoinfo = img.shape 
pwidth = (totoinfo[1]-1 )
pheight= totoinfo[0]-1 



#print (pwidth )
#print (pheight )

#ls= img.tolist()
#print (len(ls))
# 注意这里是按照 256 进行显示， 
#cv.imshow("1",img)
#cv.waitKey(0


#http://hqok.net/article-843-1.html 
#  CNew = (Max(R,G,B) + Min(R,G,B)) / 2  hdr 去



maxwidth  = 0 
maxheight = 0 
colorfloat = 0 
maxinforkey =[0,0]
singlecolor  = 0.0 

for i in range (0 ,pheight):
    for j in range(0,pwidth ):
       index = img[i , j ] 
       for cc in index :
           if cc >singlecolor :
               singlecolor = cc 

       # print(index )
       colortoto =  (max(index[0] ,index[1] ,index[2] ) +min (index[0] ,index[1] ,index[2]))/2.0 
       if colortoto > colorfloat :
           colorfloat =colortoto 
           maxinforkey[0] =i 
           maxinforkey[1] = j 




print ("打印最高数值 像素位置 ") 
print ( maxinforkey )

print ("打印最高 亮度  rgb分量 ") 
print (singlecolor)



print("纬度角度 一周360度 ")
print ((( (maxinforkey[1])/pwidth ))*360.0 )

#print("经纬度 一周是 ")
 # 纬度一周按照90度来计算 


print("颜色去色后最高亮度")
print (colorfloat)















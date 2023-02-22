from __future__ import print_function 
from __future__ import division 
import os 
import cv2 as cv 
import numpy as np 
import sys 
import  math  
import codepyc.cls.get_hdri_lum as lum 



##https://stackoverflow.com/questions/1659440/32-bit-to-16-bit-floating-point-conversion 

#def halftofloat (h ):
#    f =    ((h&0x8000)<<16) | (((h&0x7c00)+0x1C000)<<13) | ((h&0x03FF)<<13);
#    a = 3.4* math.pow(10,38) 
#    return  f/a     



def  readcolor   (file  , zuobiao)  : 
    img = cv.imread(file ,flags = cv.IMREAD_UNCHANGED  )  #IMREAD_ANYDEPTH      #IMREAD_UNCHANGED
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
    #return color 
    return  ([color[2] ,color[1],color[0]])


def  read16float    (file  , zuobiao)  : 
    img = cv.imread(file ,flags = cv.IMREAD_UNCHANGED  )  #IMREAD_ANYDEPTH      #IMREAD_UNCHANGED
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

    # 16位的float 图通过cv 读出来是整数的关系， 需要利用np 进行转换 完成到浮点的操作 
    #  
    
    color =  (img[zuobiao[1] ,zuobiao[0]])
    #return color 
    tmp=np.array([color[2] ,color[1],color[0]], np.int16)
    tmp.dtype = np.float16


    return  (tmp)
    

def  write_file (file , com ) :
    st = open(file ,"w") 
    for i in com :
        a = str(i)
        st.write (a) 
        st.write("\n")

    st.close ()



def readmaxvalue (file):
    """
    获取最大数据 
    """
    img = cv.imread(file ,flags = cv.IMREAD_UNCHANGED  )  #IMREAD_ANYDEPTH      #IMREAD_UNCHANGED
    totoinfo = img.shape 
    pwidth = (totoinfo[1] )
    pheight= totoinfo[0]
    tem = None 
    temk = 0                                        
    for i in range (0 ,pheight):
       for j in range(0,pwidth ):
                tem =img[i , j ]  # 三色 c
                # print(tem)
                l= lum.get_hdri_lum().hdri_lum( [ tem[0] ,tem[1] ,tem[2]] )
                if l> temk :
                    temk = l 

    return temk  

def readmaxvalue_value (file):
    """
    获取最大数据 
    """
    img = cv.imread(file ,flags = cv.IMREAD_UNCHANGED  )  #IMREAD_ANYDEPTH      #IMREAD_UNCHANGED
    totoinfo = img.shape 
    pwidth = (totoinfo[1] )
    pheight= totoinfo[0]
    tem = None 
    temk = [] 
                                           
    for i in range (0 ,pheight):
       for j in range(0,pwidth ):
                if j== 415 :
                    tem =img[i , j ]  # 三色 c
                    # print(tem)
                    l= lum.get_hdri_lum().hdri_lum( [ tem[0] ,tem[1] ,tem[2]] )
                    temk.append((l))

    
                    
    write_file ("c:\\tmp\\t.txt", temk)






                        
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
            print (t)
                     
            temp+=t
            #print (temp)
    # 全部加在除以 
    num= pheight * pwidth  
    color =  temp / num 
    return  ([color[2] ,color[1],color[0]])

if __name__ == "__main__" :
  

    wadobergb= r"C:\tmp\camera\converted\DSC_working_adobergb.tif"
    wprophoto = r"C:\tmp\camera\converted\DSC_working_prophoto.tif"
    wsrgb =  r"C:\tmp\camera\converted\DSC_working_srgb.tif"
   

    srgb =  r"C:\tmp\camera\converted\srgb.tif"
    pro =  r"C:\tmp\camera\converted\pro.tif"
    adobe =  r"C:\tmp\camera\converted\adobe.tif"

    clmp01 = r"C:\tmp\camera_sig\converted\DSC_6031.tif"



    readmaxvalue_value(clmp01)



    #print(readcolor (wadobergb ,[30,30])  )
    #print(readcolor (wprophoto ,[30,30])  )
    #print(readcolor (wsrgb ,[30,30])  )



    # print(readcolor (pro ,[30,30])  )
    # print(readcolor (srgb ,[30,30])  )
    # print(readcolor (adobe ,[30,30])  )

    ### 图像的全景计算
    #print(readcolor (tiff16 ,[30,30])  )
    #print (read16float (tiff16float ,[30,30]) )
    #print (readcolor(tiff32float ,[30,30]) )




    # 图像彩点计算  
    #key = [2786 ,2249] 
    #onecolor =  ( readcolor (tiff ,key))
    #twocolor  =  ( readcolor (tiffcopy ,key))

    #o  = lum.get_hdri_lum().hdri_lum(onecolor)
    #o1  = lum.get_hdri_lum().hdri_lum(twocolor)
    #print("以下是没有处理白平衡之前的亮度") 
    #print (o)

    #print ("以下是处理白平衡之后的亮度") 
    #print (o1 )

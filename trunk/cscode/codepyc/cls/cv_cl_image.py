
import os 
import cv2 as cv 
import sys 
import math 

# 读写 ldr hdr 图像计算并保存  

from get_hdri_lum import  get_hdri_lum 

    #https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#display-image
    # 图像显示过程 
    # cv.namedWindow("im",cv.WINDOW_NORMAL)  # 创建标准窗口吧图像放进去  
    # cv.imshow("im" ,im )
    # cv.waitKey(0) 
    # cv.destroyAllWindows()

    # 写图像 
    # cv.imwrite(newfile , im  )


    # k = cv.waitKey(0) 
    # print (ord ("s" ) ) # 转成数 


print ( cv.__version__ )

# 根据不同亮度保存图像
def  openldrimage (file  ) :
    im = cv.imread(file   ,flags = cv.IMREAD_COLOR)  

    wdith = ( im.shape)[1]
    height = ( im.shape)[0]
    # ldr 是 0-255 所以要转 0-1 
    pn =  os.path.dirname(file )
    name =  os.path.splitext( (os.path.basename( file)))[0]
    ppname = os.path.splitext( (os.path.basename( file)))[1]
    eye= pn +"\\"+ name+ "_eye" +ppname 
    ps =   pn +"\\"+ name+ "_ps" +ppname 
    normal =  pn +"\\"+ name+ "_normal" +ppname 
    cus =  pn +"\\"+ name+ "_cus" +ppname 


    oop = get_hdri_lum()
    eye_im =  im.copy()
    ps_im  = im.copy() 
    normal_im = im.copy() 
    cus_im = im.copy()

    for i in range ( 0, height) :
        for j in range (0, wdith):
            newcolor = im[i,j ]
            nor_color = newcolor/255.0 
            eye_num  = math.ceil (oop.hdri_eye( nor_color)*255.0  )
            eye_im[i,j] = [eye_num,eye_num,eye_num]

            ps_num  =   math.ceil (oop.hdri_ps( nor_color)*255.0 )
            ps_im [i ,j ] = [ps_num,ps_num,ps_num] 


            normal_num =   math.ceil (oop.hdri_lum( nor_color)*255.0 ) 
            normal_im[i,j] = [normal_num,normal_num,normal_num] 

            cus_num  = math.ceil(oop.hdri_cus( nor_color *255.0 ))
            cus_im[i,j]  = [cus_num,cus_num,cus_num]



    # 写数据  

    cv.imwrite( eye , eye_im )
    cv.imwrite(ps , ps_im )
    cv.imwrite (normal , normal_im )
    cv.imwrite (cus  , cus_im )





file = r'S:\hdr\2023\test\ChuangYiZ1202302201019_Abs2D3_sunOff_Srgb.hdr'

# openldrimage(file  )


# 打印几种算法 图像的最后积分数据 
def  printLdrPuls  (file  ) :
    im = cv.imread(file   ,flags = cv.IMREAD_COLOR)  

    wdith = ( im.shape)[1]
    height = ( im.shape)[0]
    # ldr 是 0-255 所以要转 0-1 
    eye_im = 0.0 
    ps_im = 0.0
    normal_im =0.0 
    cus_im = 0 

    oop = get_hdri_lum()
    for i in range ( 0, height) :
        for j in range (0, wdith):
            newcolor = im[i,j ]
            nor_color = newcolor/255.0 
            eye_num  = (oop.hdri_eye( nor_color)  )
            eye_im += eye_num

            ps_num  =   (oop.hdri_ps( nor_color) )
            ps_im += ps_num


            normal_num =   (oop.hdri_lum( nor_color) ) 
            normal_im +=normal_num 

            cus_num = ( oop.hdri_cus( nor_color))
            cus_im += cus_num 




    print ("基于人眼计算: %s " % eye_im ) 
    print ("基于ps 算法： %s " %  ps_im )
    print ("基于亮度：%s " %  normal_im ) 
    print ("基于平均数据处理：%s " % cus_im  )



# printLdrPuls(file )


def  printHdrPuls  (file  ) :
    im = cv.imread(file   ,flags = cv.IMREAD_ANYDEPTH)  

    wdith = ( im.shape)[1]
    height = ( im.shape)[0]
    # ldr 是 0-255 所以要转 0-1 
    eye_im = 0.0 
    ps_im = 0.0
    normal_im =0.0 
    cus_im = 0 

    oop = get_hdri_lum()
    for i in range ( 0, height) :
        for j in range (0, wdith):
            newcolor = im[i,j ]
            nor_color = newcolor # hdr 数据不除以255 本身就是浮点数据
            eye_num  = (oop.hdri_eye( nor_color)  )
            eye_im += eye_num

            ps_num  =   (oop.hdri_ps( nor_color) )
            ps_im += ps_num


            normal_num =   (oop.hdri_lum( nor_color) ) 
            normal_im +=normal_num 

            cus_num = ( oop.hdri_cus( nor_color))
            cus_im += cus_num 
    # print ( im[23,45])




    print ("基于人眼计算: %s " % eye_im ) 
    print ("基于ps 算法： %s " %  ps_im )
    print ("基于亮度：%s " %  normal_im ) 
    print ("基于平均数据处理：%s " % cus_im  )

# printHdrPuls(file )

def  openHdrimage (file  ) :
    im = cv.imread(file   ,flags = cv.IMREAD_ANYDEPTH)  

    wdith = ( im.shape)[1]
    height = ( im.shape)[0]
    # ldr 是 0-255 所以要转 0-1 
    pn =  os.path.dirname(file )
    name =  os.path.splitext( (os.path.basename( file)))[0]
    ppname = os.path.splitext( (os.path.basename( file)))[1]
    eye= pn +"\\"+ name+ "_eye" +ppname 
    ps =   pn +"\\"+ name+ "_ps" +ppname 
    normal =  pn +"\\"+ name+ "_normal" +ppname 
    cus =  pn +"\\"+ name+ "_cus" +ppname 


    oop = get_hdri_lum()
    eye_im =  im.copy()
    ps_im  = im.copy() 
    normal_im = im.copy() 
    cus_im = im.copy()

    for i in range ( 0, height) :
        for j in range (0, wdith):
            newcolor = im[i,j ]
            nor_color = newcolor
            eye_num  =  (oop.hdri_eye( nor_color)  )
            eye_im[i,j] = [eye_num,eye_num,eye_num]

            ps_num  =    (oop.hdri_ps( nor_color) )
            ps_im [i ,j ] = [ps_num,ps_num,ps_num] 


            normal_num =   (oop.hdri_lum( nor_color) ) 
            normal_im[i,j] = [normal_num,normal_num,normal_num] 

            cus_num  = (oop.hdri_cus( nor_color  ))
            cus_im[i,j]  = [cus_num,cus_num,cus_num]



    # 写数据  

    cv.imwrite( eye , eye_im )
    cv.imwrite(ps , ps_im )
    cv.imwrite (normal , normal_im )
    cv.imwrite (cus  , cus_im )

# openHdrimage(file )



def  readHdrPix (file , point ):
    im = cv.imread(file   ,flags = cv.IMREAD_ANYDEPTH)  

    wdith = ( im.shape)[1]
    height = ( im.shape)[0]
    
    print ( im[point[1],point[0]])



readHdrPix (file , [438 ,49 ] )
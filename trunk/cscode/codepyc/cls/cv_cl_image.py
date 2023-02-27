
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

# 打开hdr 文件 去色并保存成 4中去色模式
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

    #im = cv.imread(file   ,flags = cv.IMREAD_ANYDEPTH)  
    im = cv.imread(file   ,-1)  

    wdith = ( im.shape)[1]
    height = ( im.shape)[0]
    
    rgb = ( im[point[1],point[0]])
    print (rgb  )
    # print ( rgb[0]  ==math.n  )

# readHdrPix (file , [438 ,49 ] )

# ==读取hdr 图形最大亮度 
def  rendhdrMaxnum (flile ) :
    # 按照亮度来返回处理 
    im =cv.imread( file , -1 ) 
    wdith = ( im.shape)[1]
    height = ( im.shape)[0]
    pix =[0,0,0]
    lum =0 
    ii =0 
    jj = 0 
    error = [] 
    oop = get_hdri_lum ()
    for i in range ( 0, height) :
        for j in range (0, wdith):
            newcolor = im[i,j ]
            # print ( newcolor )


            nor_color = oop.hdri_cus(newcolor) 
            if  nor_color > lum :
                lum = nor_color 
                pix = newcolor 
                ii = j 
                jj = i 

    print("打印最亮像素" )
    print (pix )
    print ("最大亮度" )
    print ( lum )

    print ("打印坐标")
    print ( "[ {},{} ]".format ( str(ii) ,   str(jj))   )
    # return pix 




# hdr 文件传入 +  亮度显示， 超过亮度 ，就同比例缩放到该亮度关系 
# 写一个新文件 文件名称后缀clamp 
def  openHdrimageWriteClampColor  (file , lums  ,minlums ) :
    im = cv.imread(file   ,-1)  

    exr_zhi = 65503.0
    exr_num = 0.00001  

    wdith = ( im.shape)[1]
    height = ( im.shape)[0]
    # ldr 是 0-255 所以要转 0-1 
    pn =  os.path.dirname(file )
    name =  os.path.splitext( (os.path.basename( file)))[0]
    ppname = os.path.splitext( (os.path.basename( file)))[1]
    o1 = str(lums).replace('.','D')
    o2 =  str(minlums).replace('.','D')
    cus =  pn +"\\"+ name+ "_Clamp_" +o1 +"_"+ o2  +ppname 


    oop = get_hdri_lum()
    cus_im = im.copy()

    for i in range ( 0, height) :
        for j in range (0, wdith):
            newcolor = im[i,j ]
            nor_color = newcolor
            # 防止树枝出现inf nan   hdrexr 超出阈值会出现 
            if nor_color[0] == math.inf  or  nor_color[0] == math.nan  :
                nor_color[0] = exr_zhi # 波阈值小一点 
            elif nor_color[1] == math.inf or  nor_color[0] == math.nan :
                nor_color[1] =exr_zhi 
            elif nor_color[2] ==math.inf  or  nor_color[0] == math.nan :
                nor_color[2] = exr_zhi 

            # 解负数无穷大  
            if nor_color[0] == -math.inf  or  nor_color[0] == math.nan  :
                nor_color[0] = exr_num # 波阈值小一点 
                # print ("有负数")
            elif nor_color[1] == -math.inf or  nor_color[0] == math.nan :
                nor_color[1] =exr_num 
                # print ("有负数")
            elif nor_color[2] == -math.inf  or  nor_color[0] == math.nan :
                nor_color[2] = exr_num 
                # print ("有负数")


            #计算像素的亮度 
            cus_num  =   max (nor_color ) #### (oop.hdri_cus( nor_color  ))
            # min_num  = min ( nor_color )
            if lums != None :
                if  cus_num > lums :
                    # 同比例缩放 
                    fenmu = max (nor_color )
                    x = ((nor_color[0])/fenmu )*lums 
                    y = ((nor_color[1])/fenmu )*lums 
                    z= ((nor_color[2])/fenmu )*lums 
                
                    cus_im[i,j]  = [x,y,z ]
            if minlums != None :
                # 对于最小亮度提高 
                if  cus_num < minlums :
                    fenmu = max (nor_color )
                    x = ((nor_color[0])/fenmu )*minlums 
                    y = ((nor_color[1])/fenmu )*minlums 
                    z= ((nor_color[2])/fenmu )*minlums 
                
                    cus_im[i,j]  = [x,y,z ]

    # 写数据  

    cv.imwrite (cus  , cus_im )






#### 教程   
#####  file 是hdr 文件 
##### lums 是显示亮度， 输出新文件 并 后缀 clamp  
##### minlums  传入最小树枝小于该数据就提亮   
##### exr  经常会有截断问题范文出现无穷大 
####### 什么都不能处理就 写None 
# file =r'S:\hdr\2023\StandHdrpai\hdrtwo\converted\beifen\ChuangYiZ1202302201054_Abs2D11_sunOff_Srgb.exr'
# openHdrimageWriteClampColor(file , 20.0,  None  )




##### 教程 
##### file hdr 文件 
# #####  point 坐标 注意输入是 x y  横 竖  get 回来像素 注意不是rgb  而是 bgr   
# file =r'S:\hdr\2023\StandHdrpai\hdrone\converted\test_hdr_clamp\abs_srgb.exr'
# readHdrPix (file ,[1820,1780])





##### 教程 
#### file hdr exr 图形 
##### 读取图形最大亮度 返回数据 

# file =r'S:\hdr\2023\StandHdrpai\hdrtwo\converted\ChuangYiZ1202302201054_Abs2D11_sunOff_Srgb.hdr'

# rendhdrMaxnum (file )


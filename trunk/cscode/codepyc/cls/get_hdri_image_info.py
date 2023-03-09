#import __future__ 
#from __future__ import print_function 
#from __future__ import division 


import os 
import cv2 as cv 
import numpy as np 

from  cscode.codepyc.cls.get_hdri_lum import get_hdri_lum 
import cscode.codepyc.cls.get_hdri_lum 
import math







class get_hdri_image_info:
    """获取hdri图形相关信息，最亮的像素，  最高亮度的位置， 
      使用什么方法获取亮度的方法 
      """
    #hdriimg = None  
    def __init__(self, path ,HDRIEYELUM =1 ):
        self.path  = path
        self.hdriimg  = None
        self.hdriimg_8 = None   # 用来现实的hdri i 
        self.width = None 
        self.height =None
        self.keypoint = None # 用来定位最亮的像素    索引记录方式是 宽和 高 
        self.singcolorlum =None 
        self.ldrpath = None 
        self.hdri_write =None 

        # 一上来就完成这部分的函数的构造 ,防止后续在加载 贴图操作  
        self.gethdri_hightvalue_info(HDRIEYELUM)  

        # 到这里 知道构造的数据有 
        # 路径
        # hdr 信息
        # 宽高 
        # keypoint 
        # 最亮颜色
        # ldr路径
        # hdr 要写的路径 


    def openfile (self ):
         self.hdriimg  = cv.imread(self.path  ,flags = cv.IMREAD_ANYDEPTH) 
        # 处理hdri 数据 
         ldrpatharray  =os.path.splitext(self.path) 
                   
         self.ldrpath  =ldrpatharray[0]+ "_tonemap.png" 
         self.hdri_write =  ldrpatharray[0] + "_SF.hdr" 



    def gethdri_size (self )  :
        a = (0,0)  
        # 这部分进行优化都放到构造函数中 

        #if self.hdriimg != None :
        #    totoinfo = self.hdriimg.shape 
        #    pwidth = (totoinfo[1] )
        #    pheight= totoinfo[0] 
        #    a = (pwidth ,pheight)
        #else:
        #    self.openfile()
        #    totoinfo = self.hdriimg.shape 
        #    pwidth = (totoinfo[1] )
        #    pheight= totoinfo[0] 
        #    a = (pwidth ,pheight)

        self.openfile()
        totoinfo = self.hdriimg.shape 
        pwidth = (totoinfo[1] )
        pheight= totoinfo[0] 
        a = (pwidth ,pheight)
        self.width = pwidth 
        self.height = pheight
        return a 


    def gethdri_hightvalue_info (self, HDRIEYELUM =1 ):
        """ 分布获取 最高亮度和坐标 
            注意这里获取是rgb 分量的最高亮度
            最后一个计算的是平均亮度 
            HDRIEYELUM 是计算亮度的方法  枚举类型 123 
        """
        singlecolor= 0.0 
        keypoint =[0,0]
        singlum = 0.0 

        # 这部分统一放到构造函数中，一上来就完成这部分的操作 
        #if self.width ==None or self.height == None :
        #    self.gethdri_size()

        self.gethdri_size()
        for i in range (0 ,self.height):
            for j in range(0,self.width ):
               index = self.hdriimg [i , j ] 
               for cc in index :
                   if cc >singlecolor :
                       singlecolor = cc 
                       keypoint = [j,i] 
        self.keypoint = keypoint
 
        keypoint_x = self.keypoint[0] /self.width 
        keypoint_y = self.keypoint[1] / self.height
        
       

        if  HDRIEYELUM == 1 :
            rgb = self.hdriimg [self.keypoint[1] ,self.keypoint[0]] 
            lobj = get_hdri_lum()
            ll = lobj.hdri_ps (rgb)
            singlum = ll
        elif HDRIEYELUM == 2 :
           
            rgb = self.hdriimg [self.keypoint[1] ,self.keypoint[0]] 
            lobj = get_hdri_lum()
            ll = lobj.hdri_lum (rgb)
            singlum = ll
        elif  HDRIEYELUM == 3 :
            rgb = self.hdriimg [self.keypoint[1] ,self.keypoint[0]] 
            lobj = get_hdri_lum()
            ll = lobj.hdri_eye (rgb)
            singlum = ll

        self.singcolorlum = singlum
        return [singlecolor ,keypoint, singlum ]


    def ue_light_y_ratation (self, vlaue ):
        #这里是hdrit图从 0 - 180 轴向都是基于z轴的， 但是实际的 ue  是利用 到x轴的角度换算的， 
        # 这部嗯需要一个换算， 在笔记 “利用openCV 处理hdr图形” 匹配ue 旋转 有说明  
        # value 是小于等于180 的 
        key = 0
        if vlaue <=90 :
            key = 90 - vlaue 
        elif vlaue >90 :
            key = -(vlaue - 90 )

        return key 

    def  normalize_a (self, v ) :
            #
        a = math.sqrt((v[0]*v[0] + v[1]*v[1] + v[2]*v[2]))
        return  ( [v[0]/a ,v[1]/a , v[2]/a ]   ) 


    def calca_sun_dir (self ):
        #通过计算最亮颜色 坐标 ，宽高 ，还有像素的颜色亮度 
        # self.gethdri_hightvalue_info ( 1 )   # 构造完成这部分从新运算 
        # 注意因为计算在右手坐标系中计算，但是ue是是左手坐标系，  所以需要一个转换 
        # 注意图形进行 了变形这里 所以采样进行线性采样就好，轴上按照 360度进行计算 
        # 高度上向上是90度 向下也是 90度，这里从上到下平均180度处理，0-90度
        # 太阳一般都是在

        U_value  =( self.keypoint[0] /self.width  ) * 360  + 90 
        V_value  = (self.keypoint[1] / self.height )*180 

        # 公式处理方式 
        # x = cos(360 -U)*sin (V) 
        # y = sin(360 -U)*sin (V) 
        # z = cosV 

        # 注意python 是以弧度计算  选哟准一下 

        new_U_vlaue = (360 - U_value )* (math.pi / 180 )
        new_V_value = V_value * (math.pi / 180 )



        x = math.cos(new_U_vlaue)*math.sin( new_V_value) 
        y =math.sin(new_U_vlaue)*math.sin(new_V_value) 
        z =math.cos(new_V_value)


        # 方向是向内的，不是向外的  要方向 算负数  
        raw =[x,y,z ]
        raw = [ i*-1 for i in raw]   
        # newraw =  self.normalize_a(raw)     # 在计算一次 验证 

        return raw 


    def calca_sun_dir_form_vect0r (self ,sundir ):
        #   跟进太阳在图像上的点，推到出 横向对应 360  纵对应180 
        # 计算出来 太阳向量， 和ue 对应的处理 
        # 那里计算 出来 [0.059767244823854156, -0.9698499032616404, 0.23626053752066223] 
        # 方向 [1,0,0] 对应ue中的不旋转 
        #x = math.cos(360-U_value)*math.sin( V_value) 
        #y =math.sin(360-U_value)*math.sin(V_value) 
        #z =math.cos(V_value) 
        # 其实就是把他带入进去  
        V = math.acos( sundir[2])  
        U = math.acos (sundir[0] /(math.sin(V )))

        # 这里部分是对应的弧顶   转角度  
        
        Ua = U*180/math.pi
         
        Va = V*180/math.pi 
       
        return (Ua  ,Va )




    def calca_sun_in_ue_angle(self ):
        '''
        返回的是方向交 和 天顶角度
        返回4个数值 对应ue 的灯光方向  两组 
        1  计算方向角度做过90度偏移
        2 计算天顶角以ue为准
        3 计算正常的方向角度
        4 计算天顶角以ue为准

        '''
        # 这里不转向量采用直接除法计算  
        # 
        #  
        # 20210604  针对引擎不需要处理 角度转向量， 对于
        # calca_sun_dir     calca_sun_dir_form_vect0r  函数的转换不需要了 ， 
        # 研究知道更重要的是 知道灯光的旋转坐标 其实就是在左手坐标系中， 
        # 另外知道知道 本来hdri 贴图 ue 就是直接使用的左手坐标系，+ 90 是测试出来的
        #  整个分析过程参照  
        # 在ue中 太阳旋转角度 


        #self.gethdri_hightvalue_info ( 1 )
        # 第一次加载 全部构造完成，这里不在需要处理 


        U_value  =( self.keypoint[0] /self.width  ) * 360 + 90 
        V_value  = (self.keypoint[1] / self.height )*180 

        new_v = self.ue_light_y_ratation(V_value)

        # 2021 06 11 说明一下 这里是  逻辑写道 ui 模块了 直接转uv 目前计算出来式灯光从中心照射过去
        # 需要计算 反向的方向  
        U =  math.fmod( (math.fmod ( U_value ,360 ) +180), 360 )   # 偏移90度会超过360 做一次fomd 然后 翻转 + 180 做一次fmod 
        V = new_v*-1  #应为总角度是0 -180 计算出来基于平面的相对角度 这里做反想就好了   

        # 在计算一个没有90 度偏移的  
        Uno90 =  ( self.keypoint[0] /self.width  ) * 360
        U90 = math.fmod(  (Uno90+180), 360 )



        return [U , V  ,U90 ,V ]



    def calca_indexarray_color_lum (self ,indexarray , HDRIEYELUM=1 ) :
        """ 
            注意通过比较会有一些索引数值，放到数组中  
            biru [ [2,3] ,[3,4]]
            其实 23 34 这些数字器是索引， 会根据hdri 索引图片来找到 颜色数值 浮点类型 [x y z ] 
            这里是根据索引浮点类来 计算出来平均亮度 
               HDRIEYELUM 是计算亮度使用的方法，  有 1 2 3 ， 分别对应的是
              ps 默认去色 
              计算像素的亮度
              基于人眼睛计算亮度 
        
        """

        lum = 0 
        ioo = 0 
        listcolorlum = []
        ##if self.hdriimg.all() != None :  # 操作时候 多半这里不会是none 
               
        singlum= 0 
        for  keypoint  in  indexarray  :
            rgb =  self.hdriimg[keypoint[1] ,keypoint[0]] 
            # keypoint 计算使用的宽高 处理， 但是索引使用 高宽， 先确定那一行在确定行的列 
            if  HDRIEYELUM == 1 :
                lobj = get_hdri_lum()
                ll = lobj.hdri_ps (rgb)
                singlum = ll
            elif HDRIEYELUM == 2 :
                lobj = get_hdri_lum()
                ll = lobj.hdri_lum (rgb)
                singlum = ll
            elif  HDRIEYELUM == 3 :
                lobj = get_hdri_lum()
                ll = lobj.hdri_eye (rgb)
                singlum = ll
            listcolorlum.append(singlum)
              # 计算亮度平均
        for i in listcolorlum :
            lum = lum + i 
            ioo+=1 
        # 传入数值不会是零， 最后分母这里可以使用 
        return  (lum /ioo)


    def array_subduction (self , bigarray ,smallaray ) :
        #实现大数组减去小数组 
        temarray = [] 
        for i in bigarray :
            if i in smallaray :
                pass 
            else:
                temarray.append(i) 
        return   temarray 


    def debug_hdri_lum (self  ,num =1   ) :
        """
            num 是传入一个数字 主要是用来实现对于自己数据数值 
            实例化构造一个hdri 对象后 
            根据传入的num 来围绕 最亮像素进行循环 
            返回 数值 有3项 
            1 最亮像素索引 
            2 最亮像素 num圈的 实体块 
            3 最亮像素每次去中心化 亮度 

                            
        """ 

        #  构造函数统一处理，这部分不在需要 
        #if self.keypoint == None :
        #    self.gethdri_hightvalue_info( 1 ) 


            #    主要是知道宽高  ，和最亮的 宽高坐标， 

        # num /宽度 是要计算的 宽度查的内容 
        # 根据keypoint 记录数据其实是记录的hdri 最亮限速key 
        width_vlaue = num / self.width ; 
        height_vlaue = num / self.height ; 

        # 因为keypoint 索引从0开始 下面的做法就变成了比值 最大是 a-1/a  最小是0 
        # 是想叫最小是 1/a  最大时 a/a  所以这里对于index 进行了加1 运算  
        keypoint_x = (self.keypoint[0] + 1 ) /self.width 
        keypoint_y = (self.keypoint[1] + 1 ) / self.height


        #------------------------------------------------- 去掉------------------------------------
        #### 具体过程是， 操作人员写入距离最亮的点的周边距离， 比如是3 
        #### 此时会围绕最亮点比较出来 横向 竖直方向像素， 注意由于是计算 一圈的平均亮度
        #### 比如在循环第一圈时候，减去0 圈， 独立出来第一圈  
        #### 计算 
        #### 限速的索引从0 开始 ，   
        ###for i in range (0 ,self.height):
        ###    for j in range(0,self.width ):
        ###       #A 时循环运动
        ###       A_i_vlaue = (i+1) /self.height 
        ###       A_j_vlaue = (j+1) /self.width 
        #------------------------------------------------- 去掉结束------------------------------------

        toto_color_index = [] # 总的数据储存 

        toto_color_index .append ([self.keypoint] ) 

        for i  in range(1,(num+1)):
            #这里深入时3 保证运行3次 ，分别3次加入 1/a 的变化   
            # 同时计算出来 min max 对角，直接内部循环 
            wmax =0 
            win  =0 
            hmax =0 
            hmin =0

            wmax =self.keypoint[0]+i  
            hmax =self.keypoint[1]+i 

            wmin =self.keypoint[0]-i 
            hmin = self.keypoint[1]-i 

            #对于超过范围的做一定的限制操作 
            if   wmax> self.width :
                wmax = self.width 
            if wmin < 0 :
                wmin = 0 
            if hmax > self.height :
                hmax =self.height 
            if hmin < 0 :
                hmin = 0 

            # 测试测试对于max min 做了限制    

            #在现实范围做循环 一次加入
            tempoint = []
            
            for i in range (hmin ,hmax+1):
                for j in range(wmin,wmax+1 ):
                   temkeypoint = [j ,i ] # 这里时放入的狂高处理  
                  # print(temkeypoint)
                   tempoint.append(temkeypoint) 

            # 经过上面操作把块索引加入到 大容器中   

            toto_color_index.append(tempoint)


        #for i in toto_color_index :
        #    print("打印连续索引")
        #    print(i)

        # toto_color_index对其求出边的平均处理  
        # 
        newtoto_color_index = []  # 新的数组序列   
        for na   in  range(0, len(toto_color_index))  :
            # na 是  toto_color_index 的 索引   
            if na  > 0 :
                temary = self.array_subduction( (toto_color_index[na]) ,(toto_color_index[na-1]))
                newtoto_color_index.append(temary)

       
        #for i in newtoto_color_index :
        #    print("打印连续索引")
        #    print(i)

        onekeypoint =[self.keypoint] 
        
        del toto_color_index[0] 
        
        return  [onekeypoint , toto_color_index , newtoto_color_index ] 

    def print_debug (self ,  num =1 , HDRIEYELUM =1):
        """ 
              num 是
        
        """
        #计算debug 亮度信息在这里体现  
        gettotoinfo =  self.debug_hdri_lum(num) 
        printinfor = [] # 最后用来打印的数据信息 
        #printinfor.append("以下是debug hdri图片的信息")
        #printinfor.append("\n")

        printinfor.append("扩展检查数量是:" + str (num))


        lu = self.calca_indexarray_color_lum (gettotoinfo[0],HDRIEYELUM  )
        printinfor.append("最高像素亮度："+ str (lu))
        printinfor.append("最高像素索引："+ str ( self.keypoint))
        rgb =  self.hdriimg[self.keypoint[1] ,self.keypoint[0]] 
        printinfor.append("最高亮度颜色数值："+ str(rgb)  )
        rgbmax = max([rgb[0],rgb[1],rgb[2]])
        rgblist = [rgb[0]/rgbmax , rgb[1]/rgbmax ,rgb[2]/rgbmax  , rgbmax ]
        printinfor.append("最高亮度颜色变换到ue中的数值："+ str(rgblist)  )



        



        printinfor.append("检查最大像素数量是：" + str ((num*2)*(num*2))   )
 
        printinfor.append("以下是基于最高亮度 块平均数值:::::::: ")
        ioo = 0 
        for i in   gettotoinfo[1]:
            ioo +=1 
            printinfor.append("以下打印第" + str(ioo) +"圈 块的平均亮度" ) 
            lu = self.calca_indexarray_color_lum (i,HDRIEYELUM  )
            printinfor.append( str (lu))

        printinfor.append("\n") 
        ioo = 0 
        for i in   gettotoinfo[2]:
            ioo +=1 
            printinfor.append("以下打印第" + str(ioo) +"圈【单边】 的平均亮度" ) 
            lu = self.calca_indexarray_color_lum (i,HDRIEYELUM  )
            printinfor.append( str (lu))


        return  printinfor 


        
       # for i in    printinfor :print (i)
        
        
    def hdri_tonemap_ldr (self ): 
        # 在构造函数中统一处理 
        #if self.hdriimg.all() ==None :
        #    self.gethdri_size() 

        ldrpath =self.ldrpath 

        # 图形映射成8 位
        tonemapDrago  = cv.createTonemapDrago(1.0,0.7) 
        ldrDrago = tonemapDrago.process(self.hdriimg)
        ldrDrago = 3 * ldrDrago*255;
        mv =  max(self.height , self.width) 
        fc =  1/(mv / 128.0)    # 缩放因子 
        w = fc  
        h =  fc 
        newa = cv.resize(ldrDrago ,None,fx =w,fy = h,interpolation = cv.INTER_LINEAR)
        cv.imwrite (ldrpath , newa )





if __name__ =="__main__" :
   hdrpath = r"L:\Project\temp\reader_write_hdr\TrueHDRI_190111EitaiBridgeA_L1000_SunOff_camera_256.hdr"
   cc = get_hdri_image_info(hdrpath)
  # print (cc.gethdri_hightvalue_info(1))
   print (cc.ue_light_y_ratation(123))

   
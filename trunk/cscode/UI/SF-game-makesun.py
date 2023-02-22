import sys
#import   PyQt6.QtWidgets
#import  PyQt6.QtCore 
#import   PyQt6.QtGui
import   PyQt6.sip 
from PyQt6.QtWidgets import QApplication ,QWidget ,QLineEdit ,QHBoxLayout ,QVBoxLayout  ,QPushButton  ,QLabel ,QSpinBox ,QComboBox,QListWidget ,QAbstractItemView \
    ,QDialog  ,QFileDialog  , QMessageBox , QDoubleSpinBox 
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QImage ,QIcon ,QPicture,QPixmap 



from codepyc.cls.get_hdri_image_info import get_hdri_image_info 


import time 
import numpy as np 
import cv2 as cv 
import os


# 作者： tanpei 
# 时间： 2021 5月底 6月初 
# 关于hdri 照明摄影理解 有    liamllchen  sittwang 相助 
# 关于程序hdri 图片处理算法部分 有  lendyzhang 相助  
# 关于思路梳理部分 有    zhengyhuang 相助 



class MyApp (QWidget) :
    def __init__(self) :
        super().__init__()
        # 这部分是自定义 
        self.setWindowTitle("SF-Game-HDRITools-tanpei20210601 ")
        self.window_width, self.window_height = 500, 800
        self.resize(self.window_width, self.window_height)
        self.iq = QIcon("ico32.ico")
        self.setWindowIcon(self.iq)

        self.hdri_info = None  # 防止出现问题  
        self.hdri_path =None 
        self.new_ldr_path =None 
        

        self.layout = QVBoxLayout() 
        self.setLayout(self.layout)

        


        self.h1 = QHBoxLayout()
        self.input = QLineEdit()
        self.input.setPlaceholderText( "")
        self.input.setReadOnly(True)



        self.getpath = QPushButton()
        self.getpath.setText ("获取路径")

        self.h1.addWidget(self.input)
        self.h1.addWidget(self.getpath)


        self.h2 = QHBoxLayout()
        self.imw =QLabel ()
        self.imw.setFrameStyle(1)


        self.h2.addWidget(self.imw)


        self.h3 = QHBoxLayout()
        self.vl = QSpinBox()
        self.vl.setRange(1,500)
        self.vl.setValue (2)
        self.vl.setSingleStep(1)
        self.btn0 = QPushButton("HDRI 太阳的亮度衰减 ") 

        self.btn = QPushButton("计算hdri图太阳的方向") 
        self.h3.addWidget(self.vl)
        self.h3.addWidget(self.btn0,1)
        self.h3.addWidget(self.btn,2)


        self.h4 = QHBoxLayout()
        self.ls = QComboBox()
        self.ls.addItems(["默认ps去色算法","PS中亮度算法","PS中的基于人眼睛亮度算法"])

        self.h4.addWidget(self.ls)

        self.h5 =  QHBoxLayout()
        self.lv = QListWidget()
        #self.lv.addItems(["tset" ,"t"])

        self.mm =QAbstractItemView.SelectionMode(2) 
        self.lv.setSelectionMode( self.mm )
        self.h5.addWidget(self.lv)
        

        

        self.btn1 = QPushButton("拷贝列表内容，到剪切版 ") 


        self.h6 =  QHBoxLayout()
        self.sp1 =  QDoubleSpinBox()
        self.sp1.setRange(-99999.0 ,2147483647000.0)
        self.sp1.setValue (1.0) 

        self.btn2 = QPushButton("涂抹亮度.同目录另存_sf.hdr 文件  ")
        
        self.h6.addWidget(self.sp1 ,1 )
        self.h6.addWidget(self.btn2,2)



        # 总的框架 加入 
        self.layout.addLayout(self.h1)
        self.layout.addLayout(self.h2,2)
        
        self.layout.addLayout(self.h3)
        self.layout.addLayout(self.h4)
       
        self.layout.addLayout(self.h5,5)
        self.layout.addWidget(self.btn1)

        self.layout.addLayout(self.h6)




        # 链接事件  
        self.input.inputRejected.connect(self.calltest)
        self.btn1.clicked.connect(self.copys)

        self.getpath.clicked.connect (self.openfilepath)
        self.btn2.clicked.connect (self.write_hdri_data  )

        self.btn0.clicked.connect(self.clca_hdri_color)
        self.btn.clicked.connect(self.calca_hdri_sun_dir)  #计算太阳方法 



    def unmmap (self,minv ,maxv , val , tomin ,tomax ) :
        #传入一个数值最低最高， 然后做一个对应的映射关系 
        a = maxv - minv 
        a1= val - minv 
        b = tomax - tomin 


        x= (a1/a)*(tomax - tomin)+ tomin  
        # 注意x其实是变换后结果亮度， 需要直接得到比例 
    
        return (  x /val )


    def calltest (self):
        print ("进行了更改" )


    def  calca_hdri_sun_dir (self ): 
          if  self.hdri_info !=None :
              # 用来说明需要先加载hdr 文件处理 
            algle =   self.hdri_info.calca_sun_in_ue_angle()
            print_info = []
            print_info.append("以下是 根据hdri 高动态图 计算映射UE中 平行光具体旋转：") 


            print_info.append("以下是cube模式 UV接缝在 y轴正方向：") 
            print_info.append("Z 轴的旋转数[方向角]：" + str (algle[0] ) )
            print_info.append("Y 轴的旋转数[天顶角]：" + str ( algle[1]) )

            print_info.append("\n") 
            print_info.append("以下是场景采集模式 UV接缝在 x轴正方向：") 
            print_info.append("Z 轴的旋转数[方向角]：" + str ( (algle[2])  ) )   # 因为前面由偏移 90 
            print_info.append("Y 轴的旋转数[天顶角]：" + str ( algle[3]) )


            self.lv.clear()
            self.lv.addItems(print_info)
          else:
            ms=QMessageBox() 
            ms.setText("请先 打开hdr 文件 ") 
            ms.setWindowTitle("tanpei ")
            ms.exec()




    # 拷贝对象到
    def copys (self ):
        s= self.lv.count()
        sss=""
        for i in range(0,s):
            txt = self.lv.item(i)
            sss+=txt.text()
            sss+="\n"

        QApplication.clipboard().setText (sss)


    def openfilepath (self):
        
        self.d =QFileDialog.getOpenFileName(self,"打开hdri文件","",";hdri (*.hdr)")
       # print( self.d )
        if self.d[0] != "" :
            self.input.setText (self.d[0]) 
            self.hdri_path =    self.d[0]

            # 这里是要进行hdri 类的实例化处理
            # 并并类的信息 放入到了 hdri_info  中
            # 
            valtype =self.ls.currentIndex () + 1    # 主要是对用hdri 方法    
            self.hdri_info = get_hdri_image_info(self.hdri_path ,valtype) 
            #
            # 保存一下# png 图片 这里要做一个等待 
            self.hdri_info.hdri_tonemap_ldr() 
            # time.sleep(5) 
            # 加载png 
            self.new_ldr_path = self.hdri_info.ldrpath 
        
            self.ppp = QPixmap(self.new_ldr_path) 
            self.imw.setPixmap(self.ppp) 
            self.imw.setScaledContents(True)


        

    def write_hdri_data (self ) :
        # 对待用np数据 opencv来写太阳，
        #  注意 首先是计算出来 hdr 最高亮度 ， 
        #  比如设置 50 阈值 ， 最高亮度是 4000 拿就是 就是所有 像素都乘以 50/4000  
        # 注意 这里是全图扫描， 如果是室内可能会有超过该像素的 第二个灯光， 这里也一起涂抹掉 

        fazhi = self.sp1.value()  ; # 设置的阈值 
        valtype =self.ls.currentIndex () + 1    # 主要是对用hdri 方法  
        img_lum = np.copy ( self.hdri_info.hdriimg) 
        # 注意不影响原来数据， 直接拷贝一份更改   
        # 具体些的逻辑放到这里  
        #  开始构造中统一完成  
        #self.hdri_info.gethdri_hightvalue_info( valtype )
            

        ww = self.hdri_info.width 
        hh = self.hdri_info.height  
        whdri = self.hdri_info.hdri_write  # 要些hdri 的文件的名称 
        singlum = self.hdri_info.singcolorlum   # 最亮颜色 



        for i in range (0 ,hh):
            for j in range(0,ww ):
                temlum = self.hdri_info.calca_indexarray_color_lum([[j,i ]] ,valtype ) # 当前像素的亮度 
                # 根据选择计算亮度 
                if  temlum >    fazhi :
                    # 当亮度大于阈值 才进行二次处理  
                    #lumbi = (temlum -  fazhi) / singlum    # 亮度比值 该数值是该颜色
                    lumbi = self.unmmap(fazhi ,singlum ,temlum ,fazhi,(fazhi+0.1))

                    keycolor = self.hdri_info.hdriimg[i , j ] # 具体的颜色 
                    r =keycolor[0]* lumbi
                    g =keycolor[1]*lumbi 
                    b= keycolor[2]*lumbi 

                    newcolora  = np.array([r ,g, b ]) 
                    img_lum[i , j] = newcolora 

        # 写出新的hdri 图 
        cv.imwrite(whdri , img_lum )
        ms=QMessageBox() 
        ms.setText("保存，完成 ") 
        ms.setWindowTitle("tanpei ")
        ms.exec()


    def clca_hdri_color (self ) :
         
        if self.hdri_path != None : 

            # 打印hdri信息  
            val = self.vl.value()  ;
            valtype =self.ls.currentIndex () + 1    # 主要是对用hdri 方法  
        
            # 采用一次构造
            #hdrpath = self.hdri_path  # r"L:\Project\temp\reader_write_hdr\testh.hdr"
            #cc = get_hdri_image_info(hdrpath)

            listinforarray =  self.hdri_info.print_debug(val , valtype) 
            self.lv.clear()
            self.lv.addItems(listinforarray)
        else:
            ms=QMessageBox() 
            ms.setText("请先 打开hdr 文件 ") 
            ms.setWindowTitle("tanpei ")
            ms.exec()


    def test_load (self) :
        #  测试加载 
        # 测试 
        self.ppp = QPixmap(r"L:\Project\temp\reader_write_hdr\TrueHDRI_190111EitaiBridgeA_L1000_SunOff_camera_256_tonemap.png") 
        self.imw.setPixmap(self.ppp) 
        self.imw.setScaledContents(True)



            

        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyleSheet('''
    #    QWidget {
    #        font-size: 14px;
    #    }
    #''')

    myapp= MyApp() 
    myapp.show()
    sys.exit(app.exec())

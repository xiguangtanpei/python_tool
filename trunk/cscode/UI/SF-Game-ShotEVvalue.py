
# ev 射击 计算ev的拍摄次吃

from os import TMP_MAX
import sys
#import   PyQt6.QtWidgets
#import  PyQt6.QtCore 
#import   PyQt6.QtGui
import   PyQt6.sip 
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QImage ,QIcon ,QPicture,QPixmap 







import codepyc.camera.cal_ev as cev 


# 建立一个ev表 超过了 做一些nd 虚拟过程， 然后通过填写 列出要拍摄的东西 
# 我需要知道一个最低 最高， 最高呢是虚拟的，一种针 极限8000 计算  一种针对 理光的处理    

# 注意下面是针对 理光 
hLabel_one = ["EV" ,"Shutter","-EV" ,"Virtual" ,"ND2","ND4","ND8","ND16" ,"ND32","ND64","ND128","ND256","ND512","ND1024","ND2048","ND4096","ND8192"]
Hcount_one = 17
Vcount_one = 22 

EV_one = [0 ,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
EV_F_one = ["1/25000","1/12500","1/6400","1/3200","1/1600","1/800","1/400","1/200","1/100","1/50","1/25","1/13","1/6","1/3","1/1.6","1.3","1.6","3.2","6","13","25","60"]
EV_F_fu_one = ["1/25000" ,"1/50000" , "1/100000","1/200000","1/400000","1/800000","1/1600000","1/3200000","1/6400000","1/12800000","1/25600000","1/51200000","1/102400000","1/204800000","1/409600000","1/819200000","1/1638400000","1/3276800000","1/6553600000","1/13107200000","1/26214400000","1/52428800000"]


# 下面是 一般单反相机的的数据 

hLabel_two = ["EV" ,"Shutter","-EV" ,"Virtual" ,"ND2","ND4","ND8","ND16" ,"ND32","ND64","ND128","ND256","ND512","ND1024","ND2048","ND4096","ND8192"]
Hcount_two = 17
Vcount_two = 20

EV_two = [0 ,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
EV_F_two = ["1/8000" ,"1/4000" , "1/2000" ,"1/1000" ,"1/500" ,"1/250" ,"1/125" ,"1/60" ,"1/30" ,"1/15" ,"1/8" ,"1/4","1/2","1/1","2","4","8","15","30","60"]
EV_F_fu_two = ["1/8000" ,"1/16000" ,"1/32000" ,"1/64000" ,"1/128000","1/256000" ,"1/512000","1/1024000" ,"1/2048000","1/4096000" , "1/8192000" ,"1/16384000" ,"1/32768000" ,"1/65536000" ,"1/131072000" ,"1/1/262144000" ,"1/524288000","1/1048576000","1/2097152000","1/4194304000"]














class MyApp (QWidget) :
    def __init__(self) :
        super().__init__()
        # 这部分是自定义 
        self.setWindowTitle("计算 EV 拍摄次数 ")
        self.window_width, self.window_height = 1150, 650
        self.resize(self.window_width, self.window_height)

        self.hdri_info = None  # 防止出现问题  
        self.hdri_path =None 
        self.new_ldr_path =None 
        

        self.layout = QVBoxLayout() 
        self.setLayout(self.layout)

        self.h0 = QHBoxLayout() 
        

        self.ro1 =QRadioButton("理光相机EV模式") 
        self.ro2 =QRadioButton("单反相机EV模式") 
        self.ro1.setChecked(True)


        self.h0.addWidget(self.ro1)
        self.h0.addWidget(self.ro2)



        self.v1 =  QVBoxLayout() 
        
        self.tab1 = QTableWidget()
        self.cal_setev()

        # self.tab1.setEnabled(False)
        self.tab1.setColumnWidth(3,130)


        

        self.layout.addLayout(self.h0)
        self.v1.addWidget(self.tab1) 
        self.layout.addLayout(self.v1)



        # 绑定 
        self.ro1.toggled.connect(self.ro1_env)


        


    def setev (self , num  ,cum   ) :
        """
        num 是传入ev数据 
        cum 是 哪一行数据 
        i 是那一行数据的第几个 
        """
        self.tab1.setRowCount ((Vcount_one)) 
        self.tab1.setColumnCount((Hcount_one))
        self.tab1.setHorizontalHeaderLabels(hLabel_one)
        temv = []
        for i  in range(Vcount_one) :
            bb = str("")
            temv.append(bb)

        self.tab1.setVerticalHeaderLabels(temv)
        

        
        for i in range(Hcount_one) :
            self.tab1.setColumnWidth(i,60)
            self.tab1.setRowHeight (i,2)

        for i in range (Vcount_one):
            # EV 
            taa= QTableWidgetItem( str(EV_one[i]) )
            taa.setTextAlignment(4)
            self.tab1.setItem(i,0 ,taa)
            # 开门
            taa= QTableWidgetItem( str(EV_F_one[i]) )
            self.tab1.setItem(i,1, taa )

            # 虚拟EV 
            taa= QTableWidgetItem( ( "-" +str(EV_one[i])) )
            taa.setTextAlignment(4)
            self.tab1.setItem(i,2 ,taa)

            # 虚拟快门
            if i < len(EV_F_fu_one) :
                taa= QTableWidgetItem(  ("-"+ str(EV_F_fu_one[i]) ))
                taa.setTextAlignment(4)
                self.tab1.setItem(i,3 ,taa)


        num = num 
        Tmp =  []
        for i in range(num) :
            t = EV_F_one[i]
            Tmp.append(t)
        ttt = Tmp[::-1]


        ioo = 0 
        for i in  ttt :
            taa= QTableWidgetItem(  ( str(i) ))
            taa.setTextAlignment(4)
            self.tab1.setItem(ioo, cum,taa)
            ioo +=1 

        self.tab1.setColumnWidth(3,130)
    def cal_setev (self ) : 
        self.setev ( 2 ,4  ) 
        self.setev ( 3 ,5  ) 
        self.setev ( 4 ,6  ) 
        self.setev ( 5 ,7  ) 
        self.setev ( 6 ,8  ) 
        self.setev ( 7 ,9  ) 
        self.setev ( 8 ,10  ) 
        self.setev ( 9 ,11 ) 
        self.setev ( 10 ,12  ) 
        self.setev ( 11 ,13  ) 
        self.setev ( 12 ,14  ) 
        self.setev ( 13 ,15  ) 
        self.setev ( 14 ,16  ) 
    def cal_setev_two  (self ) : 
        self.setev_two ( 2 ,4  ) 
        self.setev_two ( 3 ,5  ) 
        self.setev_two ( 4 ,6  ) 
        self.setev_two ( 5 ,7  ) 
        self.setev_two ( 6 ,8  ) 
        self.setev_two ( 7 ,9  ) 
        self.setev_two ( 8 ,10  ) 
        self.setev_two ( 9 ,11 ) 
        self.setev_two ( 10 ,12  ) 
        self.setev_two ( 11 ,13  ) 
        self.setev_two ( 12 ,14  ) 
        self.setev_two ( 13 ,15  ) 
        self.setev_two ( 14 ,16  )



    def setev_two (self , num  ,cum   ) :
        """
        num 是传入ev数据 
        cum 是 哪一行数据 
        i 是那一行数据的第几个 
        """
        self.tab1.setRowCount ((Vcount_two)) 
        self.tab1.setColumnCount((Hcount_two))
        self.tab1.setHorizontalHeaderLabels(hLabel_two)
        temv = []
        for i  in range(Vcount_two) :
            bb = str("")
            temv.append(bb)

        self.tab1.setVerticalHeaderLabels(temv)
        

        
        for i in range(Hcount_two) :
            self.tab1.setColumnWidth(i,60)
            self.tab1.setRowHeight (i,2)

        for i in range (Vcount_two):
            # EV 
            taa= QTableWidgetItem( str(EV_two[i]) )
            taa.setTextAlignment(4)
            self.tab1.setItem(i,0 ,taa)
            # 开门
            taa= QTableWidgetItem( str(EV_F_two[i]) )
            self.tab1.setItem(i,1, taa )

            # 虚拟EV 
            taa= QTableWidgetItem( ( "-" +str(EV_two[i])) )
            taa.setTextAlignment(4)
            self.tab1.setItem(i,2 ,taa)

            # 虚拟快门
            if i < len(EV_F_fu_one) :
                taa= QTableWidgetItem(  ("-"+ str(EV_F_fu_two[i]) ))
                taa.setTextAlignment(4)
                self.tab1.setItem(i,3 ,taa)


        num = num 
        Tmp =  []
        for i in range(num) :
            t = EV_F_two[i]
            Tmp.append(t)
        ttt = Tmp[::-1]


        ioo = 0 
        for i in  ttt :
            taa= QTableWidgetItem(  ( str(i) ))
            taa.setTextAlignment(4)
            self.tab1.setItem(ioo, cum,taa)
            ioo +=1 

        self.tab1.setColumnWidth(3,130)








        # self.h1 = QHBoxLayout () 
        # self.l = QLabel ("间隔的EV范围：")
        # self.sp = QSpinBox ()
        # self.sp.setValue(8)
        # self.sp.setMinimum (0)
        # self.sp.setMaximum (9000000)


        # self.h1.addWidget (self.l) 
        # self.h1.addWidget(self.sp,1) 



        # self.h2 = QHBoxLayout () 
        # self.l1 = QLabel ("每次拍摄曝光几次EV:")
        # self.sp1 = QSpinBox ()
        # self.sp1.setValue(2)
        # self.sp1.setMinimum (0)
        # self.sp1.setMaximum (9000000)

        # self.h1.addWidget (self.l1) 
        # self.h1.addWidget(self.sp1,1) 


        # self.b = QPushButton ("计算") 
        # self.lab = QLabel ("....")
       

        # self.h1.addWidget(self.l)




        # # 总的框架 加入 
        # self.layout.addLayout(self.h1)
        # self.layout.addLayout(self.h2)
        # self.layout.addWidget(self.b)
        # self.layout.addWidget(self.lab)


        # #link 
        # self.b.clicked.connect(self.calltest)

    def  ro1_env (self ):
        self.tab1.clear()
        if self.ro1.isChecked() :

            self.cal_setev()

        if self.ro2.isChecked() :
            self.cal_setev_two() 

    def calltest  (self) :
        get =  cev.shot_value( int(self.sp.value()) ,  int(self.sp1.value())  )
        self.lab.setText(  ("需要拍摄次数："+   str(get))  )  





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



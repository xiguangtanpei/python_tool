import sys
#import   PyQt6.QtWidgets
#import  PyQt6.QtCore 
#import   PyQt6.QtGui
import   PyQt6.sip 
from PyQt6.QtWidgets import QApplication ,QWidget ,QLineEdit ,QHBoxLayout ,QVBoxLayout  ,QPushButton  ,QLabel ,QSpinBox ,QComboBox,QListWidget ,QAbstractItemView \
    ,QDialog  ,QFileDialog  , QMessageBox , QDoubleSpinBox 
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QImage ,QIcon ,QPicture,QPixmap 

import codepyc.camera.cal_ev as cev 


class MyApp (QWidget) :
    def __init__(self) :
        super().__init__()
        # 这部分是自定义 
        self.setWindowTitle("计算ND滤镜 EV ")
        self.window_width, self.window_height = 400, 255
        self.resize(self.window_width, self.window_height)

        self.hdri_info = None  # 防止出现问题  
        self.hdri_path =None 
        self.new_ldr_path =None 
        

        self.layout = QVBoxLayout() 
        self.setLayout(self.layout)

        self.h1 = QVBoxLayout () 
        self.sp = QSpinBox ()
        self.sp.setValue(8)
        self.sp.setMinimum (0)
        self.sp.setMaximum (9000000)
        self.b = QPushButton ("计算") 
        self.l = QLabel ("....")
        self.h1.addWidget (self.sp) 
        self.h1.addWidget(self.b) 
        self.h1.addWidget(self.l)




        # 总的框架 加入 
        self.layout.addLayout(self.h1)


        #link 
        self.b.clicked.connect(self.calltest)


    def calltest  (self) :
        get =  cev.aaa_evs( int(self.sp.value()))
        self.l.setText(str(get))





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

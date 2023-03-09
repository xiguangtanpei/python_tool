import sys 

from PySide2.QtWidgets import  QApplication 

from PySide2.QtCore import  QObject ,Signal ,Slot 

@Slot()
def out (stt) :
    print (stt )


class Test (QObject  ) :
    out_s = Signal(str )


aa = Test()
aa.out_s.connect ( out )

aa.out_s.emit ("new s ")



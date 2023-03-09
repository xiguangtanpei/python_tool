import queue  ;import   threading  ;import  time 

from PySide6.QtGui import * 
from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
import sys 


queueLock = threading.Lock() 
workQueue = queue.Queue(maxsize=10 ) #  这里是 10个线程
exitFlag = 0 
class myThreadq ( threading.Thread) :
    def __init__ ( self , threadID ,name , q):
        threading.Thread.__init__(self)
        self.threadID = threadID 
        self.name = name 
        self.q = q 
    def run (self ):
        print ("start " + self.name  +"\n") 
        pro(self.name ,self.q )
        print ("end " + self.name +"\n" )

def pro (threadName ,q ) :
    while not exitFlag :
        queueLock.acquire() # 队列还是用到了锁， 队列有i什么用 ？ 在执行安全是哪方面的安全呢？ 
        if not workQueue.empty():

            data = q.get ()

            queueLock.release() 
            print ( "{} processing {} {} \n".format( threadName , data , workQueue.qsize() ))
            # print ("4")
        else:
            queueLock.release()
        time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]   






class  myWid ( QWidget) :
    def __init__ (self  ) :
        super().__init__() 
        self.st  = QPushButton ("开启线程")
        self.btn =  QPushButton ( "测试顺序") 

        self.v =  QVBoxLayout() 
        self.v.addWidget( self.st )
        self.v.addWidget( self.btn )

        self.setLayout(self.v )


        self.btn.clicked.connect (self.openfiles)
        self.st.clicked.connect ( self.openThread )

    def openfiles (self ) :
        global nameList 
        global exitFlag 
        # 打开图像返回图像  并把图像加入到 队列中去 
        self.ms =  QMessageBox(self ) 
        self.ms.setWindowTitle("去色")
        self.ms.setText("确认要对选择的图像图像进行灰度处理？")
        self.ms.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel  )
        self.ms.setDefaultButton( QMessageBox.Cancel ) 
        msg =  self.ms.exec()
        # print (msg  )
        if  msg == QMessageBox.Ok   :
            # print ( "ok ")
            #打开hdr 文件多选择 
            self.dialog = QFileDialog (self )
            self.dialog.setFileMode( QFileDialog.ExistingFiles )
            self.dialog.setWindowTitle("打开多个文件转换去灰色") 
            self.dialog.setNameFilter( "*.png *.jpg") 
            if   self.dialog.exec() :
                get = self.dialog.selectedFiles() 
                # print (get )
                if  len (get )>0 :
                    nameList =get 
                    queueLock.acquire()
                    for world in  nameList :
                        workQueue.put(world)
                    queueLock.release()
                    exitFlag =0
                    self.openThread()


    
                

    def openThread (self) :
        # 打开操作 
        # 打开就开始运行线程 ???   
        global threadList 
        global nameList 
        global exitFlag
        threads = []
        threadid =1 

        for tName in threadList:
            thread = myThreadq(threadid , tName ,workQueue )
            # thread = threading.Thread( target=pro ,args= (  tName ,workQueue, ) )
            thread.start()
            threads.append(thread)
            threadid += 1

        # 填充队列也用到了锁， 这里 
        # queueLock.acquire()
        # for world in  nameList :
        #     workQueue.put(world)
        # queueLock.release()

        while not workQueue.empty():
            pass 

        exitFlag =1  
        # 如果是 0 就用不结束 

        for t in threads:
            t.join()
        print ("退出了")



    
if __name__ == "__main__" :
    app = QApplication([])
    w = myWid() 
    w.resize(200, 150)
    w.show()
    sys.exit( app.exec_()) 




















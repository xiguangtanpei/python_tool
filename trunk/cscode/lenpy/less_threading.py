import  threading 

# print ( threading.current_thread().getName() )

# print (threading.Thread ().getName() ) 

import time 
import cv2 as cv 



###############################################################  案例 ######################################
# def prints ( threadname , delay , counter ) :
#     while counter :
#         time.sleep( delay) 
#         print ( "{} {}".format( threadname , time.ctime(time.time())) )
#         counter -=1 

# class MyThread ( threading.Thread):
#     def __init__(self ,threadID , name , counter ):
#         threading.Thread.__init__(self) 
#         self.threadID = threadID 
#         self.name = name 
#         self.counter = counter 
#     def  run (self ) :
#         print ("startring :" + self.name )
#         # print ("id: " + str (self.threadID ))
#         prints (self.name , self.counter , 5 )
#         print ( "exiting : " + self.name )


    
# one =  MyThread(1 , "thread-1 " , 1 ) 
# two = MyThread (2, "thread-2" , 2 )


# # one.run()
# # two.run() 

# # one.start()
# # two.start()
###############################################################  案例 ######################################


from cscode.codepyc.cls.get_hdri_lum  import  get_hdri_lum 



import math 
import os 

def  makeImage  ( file ) :
    im = cv.imread( file ,cv.IMREAD_COLOR  )  

    new_im =  im.copy () 
    width = im.shape[1]
    height = im.shape[0] 
    oop = get_hdri_lum()
    for i in range( height) :
        for j in range( width) :
            newcolor = im[i , j ] 
            new = newcolor /255.0 

            eye = math.ceil( oop.hdri_eye( new )*255.0 )
            new_im[ i ,j ] = [eye , eye ,eye ]

    newfile = (os.path.splitext(file )[0]) + "_eye" +  (os.path.splitext(file )[1]) 

    cv.imwrite( newfile ,new_im)



class  imageobj () :
    def __init__(self,im , file , outfile , size ):
        # 把图片读取进内存， 全部 100 张读取进入， 多线程处理？ 然后 什么时候处理完成？ 
        # 如何知道， 才能进入下一步步骤 ？  
        self.im = im 
        self.file = file 
        self.outfile = outfile 
        self.size = size 



# 读取文件需要知道同步什么时候读取完成

def read_image (file ) :
    im = cv.imread( file ,cv.IMREAD_COLOR  )  

    new_im =  im.copy () 
    width = im.shape[1]
    height = im.shape[0] 
    newfile = (os.path.splitext(file )[0]) + "_eye" +  (os.path.splitext(file )[1]) 
    oop= imageobj(im ,file , newfile , ([width ,height])  )

    return oop  



# 到时候利用多线程类写 
# 写文件 不用同步， 写完就完成了
def wrrite_image ( imageobj ) :
    newfile = imageobj.outfile 
    new_im = imageobj.im 
    cv.imwrite( newfile ,new_im)








class PhotoP  ( threading.Thread):
    def __init__(self ,threadID , files  ):
        threading.Thread.__init__(self) 
        self.threadID = threadID 
        self.files = files 
    def  run (self ) :
        # print ("startring :" + self.name )
        # print ("id: " + str (self.threadID ))
        for  i in self.files :
            makeImage ( i  )
        # print ( "exiting : " + self.name )


file = r'S:\feature-render-Pake\test\2'
# print (time.ctime(time.time()))
ioo=0
totofiles = []

for (dirp  ,dirname , filen ) in os.walk( file ):
    for fi in  filen :
        ff = dirp + "\\" + fi 
        if os.path.isfile (ff) :
            #直接处理 一个线程 
            totofiles.append( ff )




tem1 =  PhotoP(1,totofiles[:50] )
tem2 = PhotoP(2,totofiles[50:100] )
tem3 = PhotoP(3, totofiles[100:])

tem1.start()
tem2.start()
tem3.start()







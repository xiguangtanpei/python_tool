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

            




class PhotoP  ( threading.Thread):
    def __init__(self ,threadID , file  ):
        threading.Thread.__init__(self) 
        self.threadID = threadID 
        self.file = file 
    def  run (self ) :
        print ("startring :" + self.name )
        # print ("id: " + str (self.threadID ))
        makeImage (self.file )
        print ( "exiting : " + self.name )





# print (os.path.splitext("c:/file/ss.d"))
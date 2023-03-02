
import threading  

import cv2 as cv 
import time 
import math 
import random 

# 多人在线全局触发
GlobalInfo = 1 

threadlock = threading.Lock() 


def  write_infor ( name , info , num  ) :
    global  GlobalInfo 
    (threadlock).acquire()
    time.sleep(num )
    GlobalInfo = info 
    print ( name  +":" + str( time.ctime(time.time())))

    (threadlock).release()




numarray =[1,9,7,4,3,1,8,3,9,2]

# print ( numarray )
# 对应的人员处理数据的次数 ，一定人一个人处理完成以后 才第二换处理  

ren = ['A','B','C','D','E','F','G','H','I','G']


threads = []

ioo =0
for  i  in ren :
    t = random.randint(1,4)
    tt = threading.Thread( target=write_infor , args=(i , (numarray[ioo]) , t ,) )
    ioo +=1
    threads.append( tt )

for i in  threads:
    i.start ()


for i in threads :
    i.join()

print ("所有线程处理完成打印：")
print (GlobalInfo )










    








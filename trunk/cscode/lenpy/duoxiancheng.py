
import time 

def ps (ts ,  t ):
    
    for i in range(3) :
        time.sleep( t )
        print ( ts +  str (i)  )


import _thread 


try :
    _thread.start_new_thread( ps , ("先运行："  , 2))
    _thread.start_new_thread( ps ,  ( "后运行" ,  4 ))

except:
    pass 





 
# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print (threadName )
     # print ( "%s: %s" % ( threadName, time.ctime(time.time()) )) 
 

def print_time1( threadName, delay):
   count = 0
   for i in range(5):
      time.sleep(delay)
      print (threadName )
     # print ( "%s: %s" % ( threadName, time.ctime(time.time()) )) 


# 创建两个线程
try:
   _thread.start_new_thread( print_time1, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time1, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")
 

while 1:
   pass









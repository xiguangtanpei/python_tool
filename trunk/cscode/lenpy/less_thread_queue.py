import queue 

# 其实 queue 我可以理解成 自己不给 线程主动加锁 ，二视 直接放到队列中 

import   threading 
import  time 



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
queueLock = threading.Lock() 
workQueue = queue.Queue(maxsize=10 ) #  这里是 10个线程




threads = []
threadid =1 

for tName in threadList:
    thread = myThreadq(threadid , tName ,workQueue )
    thread.start()
    threads.append(thread)
    threadid += 1

# 填充队列也用到了锁， 这里 

queueLock.acquire()
for world in  nameList :
    workQueue.put(world)
queueLock.release()

queueLock.acquire()
for world in  threadList :
    workQueue.put(world)
queueLock.release()


while not workQueue.empty():
    pass 

exitFlag =1


for t in threads:
    t.join()

print ("退出了")








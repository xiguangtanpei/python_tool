import queue 
import threading
import time
 
exitFlag = 0
 

workQueue = queue.Queue(maxsize=10 ) #  这里是 10个线程

print ( workQueue.empty())
import cv2 as cv 
import os  
import threading 
from cscode.codepyc.cls.get_hdri_lum  import  get_hdri_lum 
import math 


file = r'S:\feature-render-Pake\test\1'
# print (time.ctime(time.time()))
ioo=0
totofiles = []

for (dirp  ,dirname , filen ) in os.walk( file ):
    for fi in  filen :
        ff = dirp + "\\" + fi 
        if os.path.isfile (ff) :
            #直接处理 一个线程 
            totofiles.append( ff )

# 根据 100 多个图像创建很多 图像进程 


# 构造对象数组 和事件数组 
img_arrays =  [None]*len(totofiles) 
finish_events = [threading.Event() for i in totofiles ]


class  imageobj () :
    def __init__(self,im , file , outfile , size ):
        # 把图片读取进内存， 全部 100 张读取进入， 多线程处理？ 然后 什么时候处理完成？ 
        # 如何知道， 才能进入下一步步骤 ？  
        self.im = im 
        self.file = file 
        self.outfile = outfile 
        self.size = size 

# 读取文件需要知道同步什么时候读取完成

def read_image (index  ) :
    im = cv.imread( totofiles[index] ,cv.IMREAD_COLOR  )  
    file = totofiles[index]
    new_im =  im.copy () 
    width = im.shape[1]
    height = im.shape[0] 
    newfile = (os.path.splitext(file )[0]) + "_eye" +  (os.path.splitext(file )[1]) 
    oop= imageobj(im ,file , newfile , ([width ,height])  )
    img_arrays[index] = oop  
    finish_events[index ].set() 
    # return oop  # 不许哦返回 


# 到时候利用多线程类写 
# 写文件 不用同步， 写完就完成了
def wrrite_image ( imageobj ) :
    newfile = imageobj.outfile 
    new_im = imageobj.im 
    cv.imwrite( newfile ,new_im)

threads =[]
for i in range(len(totofiles)):
    t = threading.Thread(target= read_image ,args= (i,)) 
    t.start()
    threads.append(t )

# set了就不等待了 
for e in finish_events:
    e.wait()


# 测试ok 数据读取 这个快 非常的快  
# print ("完成读取操作 ")
# print (( img_arrays)[0].im  ) 


## 处理成灰色 的方案  
# oop = get_hdri_lum()
for img  in  img_arrays  :
    # newim =  img.im.copy()  
    # width = img.size[0] 
    # height = img.size[1] 
    # 每个图片独立处理 
    gray_img = cv.cvtColor( img.im, cv.COLOR_BGR2GRAY)

    # for i in range( height) :
    #     for j in range( width) :
    #         newcolor = img.im[i , j ] 
    #         new = newcolor /255.0 

    #         eye = math.ceil( oop.hdri_eye( new )*255.0 )
    #         newim[ i ,j ] = [eye , eye ,eye ]

    # 处理完成在写回去 
    img.im =gray_img 


##### 这里单独处理 完成 
#### 后续开始多线程写数据  


# print ( img_arrays[0].file  )

for i in img_arrays :
    t = threading.Thread(target= wrrite_image ,args= (i,)) 
    t.start()






 


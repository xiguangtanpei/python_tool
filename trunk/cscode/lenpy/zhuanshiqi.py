# 简化代码 


# 函数中定义函数 经常会使用到 倒是 

def  prints ( new ) :
    def add (a , b) :
        return a+b 
    
    aa = add( new [0] , new[1] )

    print (aa )
    return aa

# prints  (  [3 ,4 ]) 
#7  

##  函数中返回就函数 确实不多    就是 对于函数方法的选择  

def  maths  ( ints ) :
    def add (a , b ) :
        return a +b 
    
    def  sub (a , b) :
        return a - b
    def mul ( a , b ) :
        return a * b 
    
    if ints  ==1  :
        return add 
    if ints ==2 :
        return sub 
    if ints ==3 :
        return mul  
    

    

# print ( maths (2)( 3 ,4 ))
# print ( maths (3)( 3 ,4 ))
# # -1
# 12


# 名且传递有换个 函数  

def mul () :
    return 3 *4 


def  newmul  ( mul  ) :

    print  (mul ()) 


# newmul ( mul )
# 12


# @newmul 
# def zhuanshi  ():
#     print ("输入")
#     return True
    




import cv2 
from functools import wraps
 
def  news (lists ):
    @wraps( lists )
    def pp ( *arg ):
        im   =  lists (*arg )
        ims = cv2.cvtColor ( im , cv2.COLOR_BGR2GRAY) 
        cv2.imshow( "" ,ims  )
        cv2.waitKey(0)
 
        
    return pp 



@news 
def printlist (file ) :
    im = cv2.imread(file , flags=cv2.IMREAD_ANYCOLOR )
    return  im 
    



# printlist ( r'F:\2018091621203411.jpg'  )


#[3, 4, 5, 57] 


    

class aab (object) :
    def __init__(self  ) :
        print ("我是构建")
    def __call__(self) :
        print ("我是回调函数")
    def notify  (self) :
        pass 

newaa = aab  ( )
newaa.notify ( )
newaa()



         



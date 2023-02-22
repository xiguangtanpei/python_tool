
import math 


# 跟你nd 型号 计算出来 降低多多少个ev 
def aaa_evs   (nd ): 
    a = math.log(nd) / math.log(2)
    return  a  


def shot_value  (evrange , evstep ) :
    """
        1/8” -1/4” - 1/2” - 1” - 2” - 4”- 8”
        注意在ev表中 7 个ev 其实包含的是 6个范围， evrange 
        evstep  说明是是我几个ev 拍摄一次，  最后的出来的就是要拍摄多少次  

    """
    a= math.ceil(evrange /evstep +1) 
    return a   

 

if __name__ =="__main__" :
     print (aaa_evs (4000))
     print (shot_value(6 ,3))
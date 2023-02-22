


import math 
import numpy as np 


class camera_value :

    def __init__(self, kuaimen ,guangquan ):
        """
             根据相机的 光圈和快门 来计算ev  注意 这里iso 默认是100 
        """
        # 计算相机 ev 相关的处理形式 
        super().__init__() 
        self.kuaimen = kuaimen 
        self.guangquan = guangquan 
    def   clca_ev  (self ,iso=100):
        """
        跟进

        """
        ev= -math.log2(self.kuaimen ) + 2*math.log2(self.guangquan) - math.log2(100/iso) 
        return ev  

    def clca_ev_fancha  (self, fanchabi ) :
        """
             注意这里是传入的 图片比值， 根据对象反差比， 可以计算图像的动态范围
             这个 是一个大概数值， 保存图片本身的范围
        """
        ev = math.log10 (fanchabi)*3.32 
        return  ev 

    def cla_ev100 (self ) :
        ev100 = math.log2(self.guangquan*self.guangquan / self.kuaimen) + math.log2(100 / 100 )
        return ev100 

    #def  colorswap_xyz2rgb (self, x33  ,x3 ) :











if __name__ == "__main__" :
    ob = camera_value(1/30.0,9.0) 
    print (ob.clca_ev())
    print (ob.cla_ev100 ())
    print (math.log2(1))




 





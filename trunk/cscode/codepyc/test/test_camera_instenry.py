import math 

import codepyc.cls.get_hdri_lum as hlm 

import codepyc.cls.camera_value as cav 

# 实验 
# 测量亮度 =  ev亮度 * 颜色亮度 * 计算出来的系数  

# pi= 3.1415926 
# # 测量在  文件房间 
# shi_lum = 76.1/pi 
# ev = cav.camera_value(1/13 ,4.0)
# aev = math.pow (2 , (ev.clca_ev()))  ;

# lum = hlm.get_hdri_lum().hdri_lum([0.346,0.356 ,0.439]) 
# #lum = 0.49 
# cal   = shi_lum/aev /lum

# print(("亮度:"+ str(lum) ))
# print (cal)


# # 测量在  测试水吧 
# shi_lum = 76.5/pi  
# ev = cav.camera_value(1/15 ,4.0)
# aev = math.pow (2 , (ev.clca_ev()))  ;

# lum = hlm.get_hdri_lum().hdri_lum([0.560,0.537 ,0.496]) 
# #lum = 0.49 
# cal   = shi_lum/aev /lum
# print(("亮度:"+ str(lum) ))
# print (cal)



# 测量在  会议室
shi_lum = 2  
ev = cav.camera_value(1/200 ,8.0)


print(ev.clca_ev() )

# aev = math.pow (2 , (ev.clca_ev()))  ;



# lum = hlm.get_hdri_lum().hdri_lum([0.857,0.856 ,0.857]) 
# #lum = 0.49 
# cal   = shi_lum/aev /lum
# print(("亮度:"+ str(lum) ))
# print (cal)



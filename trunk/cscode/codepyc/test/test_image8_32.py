from cls.get_hdri_image_info import get_hdri_image_info 
import cv2 as cv 
import math 

hdrpath =  r"L:\Project\temp\reader_write_hdr\TrueHDRI_190111EitaiBridgeA_L1000_SunOff_camera_256.hdr"

hdrdps = r"L:\Project\temp\reader_write_hdr\TrueHDRI_190111EitaiBridgeA_L1000_SunOff_camera_256_test32.hdr"

hdrdps_8 = r"L:\Project\temp\reader_write_hdr\TrueHDRI_190111EitaiBridgeA_L1000_SunOff_camera_256_test8.png" 



cc = get_hdri_image_info(hdrpath)

cc.gethdri_size()   # 实例化获取size 



# hdri tone 到8 位一个 方法，注意这里 用来 现实到控件上 
tonemapDrago  = cv.createTonemapDrago(1.0,0.7) 
ldrDrago = tonemapDrago.process(cc.hdriimg)
# 缩放一下  映射成 8位 
ldrDrago = 3 * ldrDrago*255;
                                                
# 比较一个最大数值 
mv =  max(cc.height , cc.width) 
fc =  1/(mv / 128.0)    # 缩放因子 
w = fc  
h =  fc  



newa = cv.resize(ldrDrago ,None,fx =w,fy = h,interpolation = cv.INTER_LINEAR)
 
cv.imwrite (hdrdps , cc.hdriimg )

cv.imwrite (hdrdps_8 ,  newa  )
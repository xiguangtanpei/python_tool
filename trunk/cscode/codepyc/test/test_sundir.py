
from cls.get_hdri_image_info import get_hdri_image_info 


hdrpath =  r"L:\Project\temp\reader_write_hdr\testh.hdr"
cc = get_hdri_image_info(hdrpath)
# 打印hdri 信息的元素 
print(cc.gethdri_hightvalue_info())

# 计算hdri 太阳的向量 
print (cc.calca_sun_dir())

 # 在ue中的旋转角度 
print(cc.calca_sun_in_ue_angle()) 
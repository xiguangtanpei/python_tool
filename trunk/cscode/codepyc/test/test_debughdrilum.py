
from cls.get_hdri_image_info import get_hdri_image_info 


hdrpath =  r"L:\Project\temp\reader_write_hdr\testh.hdr"
cc = get_hdri_image_info(hdrpath)

# 主要是 根据配置 打印距离最亮的点的周围亮度信息 


cc.debug_hdri_lum(1,2 )

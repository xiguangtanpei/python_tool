

# 测试 打印平均的  权重  

from cls.get_hdri_image_info import get_hdri_image_info 


hdrpath =  r"L:\Project\temp\reader_write_hdr\testh.hdr"
cc = get_hdri_image_info(hdrpath)

cc.print_debug(5,3)
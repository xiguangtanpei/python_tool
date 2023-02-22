
         
from cls.get_hdri_image_info import get_hdri_image_info 


hdrpath =  r"L:\Project\temp\reader_write_hdr\testh.hdr"
cc = get_hdri_image_info(hdrpath)

big = [[254, 126], [255, 126], [256, 126], [254, 127], [255, 127], [256, 127], [254, 128], [255, 128], [256, 128]] 
small = []

a = cc.array_subduction()

print (a )
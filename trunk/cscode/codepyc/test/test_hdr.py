from cls.get_hdri_image_info import get_hdri_image_info 
import cv2 as cv 
import math 

hdrpath =  r"L:\Project\temp\reader_write_hdr\TrueHDRI_190111EitaiBridgeA_L1000_SunOff_camera_256.hdr"

cc = get_hdri_image_info(hdrpath)

cc.hdri_tonemap_ldr() 

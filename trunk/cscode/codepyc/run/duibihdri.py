from __future__ import print_function 
from __future__ import division 
import os 
import cv2 as cv 
import numpy as np 


hdrpath = r"L:\Project\temp\reader_write_hdr\TrueHDRI_190111EitaiBridgeA_L1000_SunOff_camera_256.hdr"
hdrd  = r"L:\Project\temp\reader_write_hdr\TrueHDRI_190111EitaiBridgeA_L1000_SunOff_camera_256_h.hdr"

img = cv.imread(hdrpath ,flags = cv.IMREAD_ANYDEPTH) 
img1 = cv.imread(hdrd ,flags = cv.IMREAD_ANYDEPTH) 
                                                                      


if (img  == img1).all()  :
    print ("true") 
else:
    print ("false")                                                            


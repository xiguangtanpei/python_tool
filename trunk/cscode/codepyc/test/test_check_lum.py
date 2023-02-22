
import os 

hdrpath = r"L:\Project\temp\reader_write_hdr\TrueHDRI_190111EitaiBridgeA_L1000_SunOff_camera_256.hdr"

hdrdps   =  os.path.splitext(hdrpath)[0] +"_ps_" +  os.path.splitext(hdrpath)[1]     # ps 的去色九三 

hdrlum   =   os.path.splitext(hdrpath)[0] +"_lum_" +  os.path.splitext(hdrpath)[1]   # 亮度计算 

hdreys   =   os.path.splitext(hdrpath)[0] +"_eye_" +  os.path.splitext(hdrpath)[1]     #感知计算 

print (hdrdps)

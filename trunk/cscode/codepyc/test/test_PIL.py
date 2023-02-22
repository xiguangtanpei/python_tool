#from PIL import Image 

                                 
#path = r"C:\tmp\color\converted\8bit.tif"
#im = Image.open(path ,mode="")




import numpy
tmp=numpy.array([14613 ,14553 ,14376], numpy.int16)
tmp.dtype = numpy.float16
tmp.dtype = numpy.int8
print (tmp)

# 数据最后是 这个  [0.6353 0.606  0.5195]  

# 同样我保存32位的数值是 0.6352339  0.60619134  0.51933557  




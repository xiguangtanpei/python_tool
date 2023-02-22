



def unmmap (minv ,maxv , val , tomin ,tomax ) :
    #传入一个数值最低最高， 然后做一个对应的映射关系 
    a = maxv - minv 
    a1= val - minv 
    b = tomax - tomin 


    x= (a1/a)*(tomax - tomin)+ tomin  
    # 注意x其实是变换后结果亮度， 需要直接得到比例 
    
    return (  x /val )




for i in range(30,49):
   v =  unmmap (2,50 ,i ,2.0 ,2.3)
   print(v )


#0.19374999999999987
#0.19999999999999987
#0.20624999999999988
#0.21249999999999986
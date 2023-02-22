import math  


def  normalize_a (v ) :
        #
    a = math.sqrt((v[0]*v[0] + v[1]*v[1] + v[2]*v[2]))
    return  ( [v[0]/a ,v[1]/a , v[2]/a ]   ) 


print (normalize_a([-0.5350213050358846, -0.7162277833808375, -0.4480736161291701]))


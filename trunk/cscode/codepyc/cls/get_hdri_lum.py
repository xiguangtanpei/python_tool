

class get_hdri_lum(object):
    """description of class"""
    def hdri_ps (self, rgb):
        """ rgb 这里传入是是一个 元组和list """
        r = rgb[0] 
        g = rgb[1] 
        b = rgb[2] 
        colortoto =  (max(r,g,b ) +min (r,g,b))/2.0 
        return  colortoto 

    def hdri_lum (self,rgb):
        r = rgb[0] 
        g = rgb[1] 
        b = rgb[2] 
        newcolor_lum =     0.2126*r + 0.7152*g + 0.0722*b
        return  newcolor_lum 

    def hdri_eye (self,rgb):
        r = rgb[0] 
        g = rgb[1] 
        b = rgb[2] 
        newcolor_eye =     0.299*r + 0.587*g + 0.114*b  
        return  newcolor_eye 
    def hdri_cus ( self ,rgb ) :
        r = rgb[0] 
        g = rgb[1] 
        b = rgb[2] 
        newcolor = (r+g+b )/3.0 
        return  newcolor 




if __name__ =="__main__" :

    # 测试使用list 还有 元组都是 ok 的 是可行的 
    c= get_hdri_lum()
#     #rg=    [0.535995,0.479096,0.39466]
#    # rg=    [156/255,148/255,128/255] 
#     #print ( c.hdri_lum((23,3,4))  )
#    # print (  c.hdri_ps(rg)  )
#     rg=    [0.851,0.851,0.863] 
    
#     print (  c.hdri_lum(rg)  )
    
    rg=    [0.980903,0.025613 ,0.943802] 
    print ( c.hdri_lum(rg)  )
    print (  c.hdri_ps(rg)  )
    print (  c.hdri_eye(rg)  )

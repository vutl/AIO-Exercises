import math

def md_nre_single(y, y_hat, n, p):
    result = ((y ** (1 / n)) - (y_hat ** (1 / n))) ** p
    print(result)

#Examples:
md_nre_single( y =100 , y_hat =99.5 , n =2 , p =1)
md_nre_single( y =50 , y_hat =49.5 , n =2 , p =1)
md_nre_single( y =20 , y_hat =19.5 , n =2 , p =1) 
md_nre_single( y =0.6 , y_hat =0.1 , n =2 , p =1)
import numpy as np
import random
def replace_center_with_minus_one(d,n,m):
   
   if d<=0 :
        raise ValueError("d<=0 cannot be")
   if m>n:
        raise ValueError("m>n cannot be")
   if n<0:
        raise ValueError("n<0 cannot be")
   if m<0:
        raise ValueError("m<0 cannot be")
  
   r_array=np.random.randint(int("1"+"0"*(d-1)),int("1"+"0"*d),size=(n,n))
   start = (n - (m)) // 2
   end = start +(m) 
   r_array[start:end, start:end] = -1
   return r_array
replace_center_with_minus_one(2,5,3)

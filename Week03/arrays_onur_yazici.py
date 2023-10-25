import numpy as np
import random
def fuction_description(n,d):
   m=n-2
   if d<=0 :
        raise ValueError("d<=0 cannot be")
   if m>n:
        raise ValueError("m>n cannot be")
   if n<0:
        raise ValueError("n<0 cannot be")
   if m<0:
        raise ValueError("m<0 cannot be")
   m_array=np.random.randint(int("1"+"0"*(d-1)),int("1"+"0"*d),size=(n,n))
   m_array[1:-1,1:-1]=-1
   return(m_array)

fuction_description(4,3)

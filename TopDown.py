def ricorsione(x,y,k,di):

  if (x == 0 and y == 0):
      return  1
  if (di):
      w = 0
      if(x-1 >= 0):
          w = ricorsione(x - 1, y, k, di ) 
      if( y-1 >= 0 and k-1 >= 0):
          w +=ricorsione(x, y - 1, k - 1, not di)
      return w
  else:
      w =0 
      if(x-1 >= 0 and k-1 >= 0):
          w = ricorsione(x - 1, y, k - 1, not di) 
      if(y-1 >=0):    
         w += ricorsione(x, y - 1, k, di)
      return w
    
def contaPercorsi(n,k):
    if(n <0):
         return -1
    if(k<0):
        return -1
    if ( n == 0):
       return 0
    if ( n == 1):
        return 1
    if( k == 0 ):
        return 0
    n-=1
    x  = ricorsione(n-1, n, k, True)
    x+= ricorsione(n, n-1, k, False)
    return  x


print(contaPercorsi(15, 15))
def trovaPercorsi(x, y, k, di,mat):
 
    if (mat[x][y][k][di] != 0):
        return mat[x][y][k][di]
    
    if (x == 0 and y == 0):
        mat[x][y][k][di]= 1
  
    if (di):
        if(x-1 >= 0):
            mat[x][y][k][di] = trovaPercorsi(x - 1, y, k, di, mat) 
        if( y-1 >= 0 and k-1 >= 0):
             mat[x][y][k][di] +=trovaPercorsi(x, y - 1, k - 1, not di, mat)
        return mat[x][y][k][di]

    else:
        if(x-1 >= 0 and k-1 >= 0):
            
            mat[x][y][k][di] = trovaPercorsi(x - 1, y, k - 1, not di, mat) 
        if(y-1 >=0):    
            mat[x][y][k][di] += trovaPercorsi(x, y - 1, k, di, mat)
        return mat[x][y][k][di]
    
    
def contaPercorsi(n, k):
    
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
    
    mat = [[[[ 0 for _ in range(2)] for _ in range(k+1)] for _ in range(n)] for _ in range(n)]
    n-=1     
    return  trovaPercorsi(n - 1, n, k, True, mat) + trovaPercorsi(n, n - 1, k, False, mat)

print(contaPercorsi( 15 ,  15))
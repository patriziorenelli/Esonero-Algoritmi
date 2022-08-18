def trovaPercorsi(n, k, mat):
    for x in range(n+1):
        for y in range(n+1):
            for z in range(k+1):
                for w in range(2):
                         if x == 0 and y == 0:
                             mat[0][0][z][w] = 1
                         elif w and x-1>= 0 and y-1>=0 and z-1>=0:
                             mat[x][y][z][w] = mat[x-1][y][z][1] + mat[x][y-1][z-1][0]
                         elif w and x-1>=0 and y-1<0:
                             mat[x][y][z][w] = mat[x-1][y][z][1]
                         elif w and x-1<0 and y-1>=0 and z-1>=0:
                             mat[x][y][z][w]+= mat[x][y-1][z-1][0]
                         elif w == False and x-1>=0 and y-1>=0 and z-1>=0:
                             mat[x][y][z][w] = mat[x-1][y][z-1][1] + mat[x][y-1][z][0]
                         elif w == False and x-1>=0 and y-1<0 and z-1>=0:
                             mat[x][y][z][w] = mat[x-1][y][z-1][1]
                         elif w == False and x-1<0 and y-1>=0:
                             mat[x][y][z][w]+= mat[x][y-1][z][0]
                         

    return  mat[n-1][n][k][1] +  mat[n][n-1][k][0]
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
    return  trovaPercorsi(n-1, k, mat)

print(contaPercorsi(4  , 2  ))
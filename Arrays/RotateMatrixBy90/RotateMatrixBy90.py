from typing import *

def rotateMatrix(mat : List[List[int]]):
    # Write your code here.
    n = len(mat)
    for i in range(0, n-1):
        for j in range(i+1, n):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
    for i in range(0, n):
        for j in range(0, int(n/2)):
            mat[i][j],mat[i][n-1-j] = mat[i][n-1-j],mat[i][j]

    pass

from typing import *

def spiralMatrix(matrix : List[List[int]]) -> List[int]:
    # Write your code here.
    n = len(matrix)
    m = len(matrix[0])
    ans = []
    top, bottom, left, right = 0, n-1, 0, m-1

    while top <= bottom and left <= right:
        # Right
        for i in range(left,right+1):
            ans.append(matrix[top][i])
        top = top+1
        # Bottom
        for i in range(top,bottom+1):
            ans.append(matrix[i][right])
        right = right-1
        if top<=bottom:
            # Left
            for i in range(right,left-1,-1):
                ans.append(matrix[bottom][i])
            bottom = bottom-1
        if left<=right:
            # Top
            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])
            left = left+1
    return ans
    pass

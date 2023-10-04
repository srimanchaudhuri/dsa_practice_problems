def setZeroes(self, matrix: List[List[int]]) -> None:
        mark = 1
        n = len(matrix)
        m = len(matrix[0])
        # Marking The marker rows and columns
        for i in range(0, n): 
            for j in range(0, m):
                if matrix[i][j] == 0:
                    if j != 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
                    else:
                        mark = 0
        #Converting Non zero elements excluding marker row or column
        for i in range(n-1,0,-1):
            for j in range(m-1,0,-1):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        #Converting marker row
        if matrix[0][0] == 0:
            for i in range(1, m):
                matrix[0][i] = 0
        #Converting marker column
        if mark == 0:
            for i in range(0, n):
                matrix[i][0] = 0
        pass

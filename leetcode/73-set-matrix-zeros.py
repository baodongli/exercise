class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        lastRow = lastCol = 1
        for i in range(m):
            if matrix[i][n-1] == 0:
                lastCol = 0
                break
        for j in range(n):
            if matrix[m-1][j] == 0:
                lastRow = 0
                break
        for i in range(m-1):
            for j in range(n-1):
                if matrix[i][j] == 0:
                    matrix[i][n-1] = 0
                    matrix[m-1][j] = 0
        #print(matrix, lastRow, lastCol)
        for j in range(n - 1):
            if matrix[m-1][j] == 0:
                for i in range(m-1):
                    matrix[i][j] = 0
        #print(matrix)
        for i in range(m - 1):
            if matrix[i][n-1] == 0:
                for j in range(n-1):
                    matrix[i][j] = 0
        if lastRow == 0:
            for j in range(n):
                matrix[m-1][j] = 0
        if lastCol == 0:
            for i in range(m):
                matrix[i][n-1] = 0

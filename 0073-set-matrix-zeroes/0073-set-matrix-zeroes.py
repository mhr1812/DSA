class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix[0]),len(matrix)
        row,col = [0 for i in range(m)],[0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        for i in range(m):
            for j in range(n):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0
                    
        
                    
        
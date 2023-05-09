class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m = len(matrix[0]),len(matrix)
        visited = [[False for j in range(n)]for i in range(m)]
        ans = []
        def recur(i,j):
            visited[i][j] = True
            ans.append(matrix[i][j])
            if i-1<=j and j<n-1 and not visited[i][j+1]:
                recur(i,j+1)
            elif i<m-1 and not visited[i+1][j]:
                recur(i+1,j)
            elif j>0 and not visited[i][j-1]:
                recur(i,j-1)
            elif i>0 and not visited[i-1][j]:
                recur(i-1,j)
            else:
                return None
        recur(0,0)
        return ans
            
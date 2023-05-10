class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for j in range(n)] for i in range(n)]
        i,j,x,y = 0,0,0,1
        for k in range(1,n*n+1):
            ans[i][j] = k
            if ans[(i+x)%n][(j+y)%n]:
                x,y = y,-x
            i+=x
            j+=y
        return ans
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for i in range(n)]
        i,j = 0, 0
        dire = [0,1,0,-1,0]
        po = 0
        for a in range(1,n*n+1):
            ans[i][j] = a
            ni,nj = i+dire[po],j+dire[po+1]
            if (not 0<=ni<n) or (not 0<=nj<n) or ans[ni][nj]!=0:
                po+=1
                po%=4
                ni,nj = i+dire[po],j+dire[po+1]
            i,j = ni,nj
        return ans
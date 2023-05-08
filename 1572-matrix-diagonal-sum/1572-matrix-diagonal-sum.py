class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat[0])
        ans = 0
        for i in range(n):
            ans+=mat[i][i]+mat[n-i-1][i]
        if n%2==1:
            ans-=mat[n//2][n//2]
        return ans
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for _ in range(m-1):
            temp = [1]*n
            for i in range(1,n):
                temp[i] = temp[i-1]+dp[i]
            dp = temp
        return dp[-1]
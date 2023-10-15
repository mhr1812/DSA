mod = 10**9+7
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        pos = min(steps//2+1,arrLen-1)
        dp = [[0 for _ in range(pos+1)] for _ in range(steps+1)]
        dp[0][0] = 1
        for i in range(1,steps+1):
            for j in range(pos+1):
                dp[i][j] = dp[i-1][j]
                if j-1>=0:
                    dp[i][j] = (dp[i][j]+dp[i-1][j-1])%mod
                if j+1<=pos:
                    dp[i][j] = (dp[i][j]+dp[i-1][j+1])%mod
        return dp[steps][0]
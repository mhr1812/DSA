class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if m < k: return 0

        dp = [[int(ki == 0)] * m for ki in range(k)]
        for _ in range(n - 1):
            for i in range(k - 1, -1, -1):
                acc = 0
                for j in range(m - 1, -1, -1):
                    dp[i][j] = dp[i][j] * (j + 1) + acc
                    if i > 0: acc += dp[i - 1][j]
        return sum(dp[-1]) % (10 ** 9 + 7)
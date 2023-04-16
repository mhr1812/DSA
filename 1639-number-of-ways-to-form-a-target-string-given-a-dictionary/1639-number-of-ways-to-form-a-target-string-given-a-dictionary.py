class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, m = len(words[0]), len(target)
        dp = [1] + [0]*m
        cnt = [Counter(pos) for pos in list(zip(*words))]
        
        for i in range(n):
            for j in range(m-1, -1, -1):
                dp[j+1] += dp[j] * cnt[i][target[j]]
                dp[j+1] %= 10**9 + 7
        return dp[m]
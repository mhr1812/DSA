class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone: set() for stone in stones}
        dp[0] = {0}
        for stone in stones:
            for jump in dp[stone]:
                for x in [jump-1,jump,jump+1]:
                    if x>0 and stone+x in dp:
                        dp[stone+x].add(x)
        return len(dp[stones[-1]])>0
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        def t(l,r):
            if (l,r) not in memo:
                memo[l,r] = min([t(l,cut) + t(cut,r) + (r-l) for cut in cuts if l<cut<r] or [0])
            return memo[l,r]
        return t(0,n)
        
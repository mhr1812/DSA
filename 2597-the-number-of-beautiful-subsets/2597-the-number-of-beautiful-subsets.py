class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        def dp(a):
            if a - k in count:
                dp0, dp1 = dp(a - k)
            else:
                dp0, dp1 = 1, 0
            return dp0 + dp1, dp0 * (2 ** count[a] - 1)

        return reduce(mul, (sum(dp(a)) for a in count if a + k not in count)) - 1
        
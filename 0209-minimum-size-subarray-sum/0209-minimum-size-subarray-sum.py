class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 0
        s = 0
        default = 10**6
        minLen = default
        while True:
            if s >= target:
                l = j - i
                minLen = min(minLen, l)
                s -= nums[i]
                i += 1
            elif j < n:
                s += nums[j]
                j += 1
            else:
                break
        return 0 if minLen == default else minLen
                
            
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = int(1e9+7)
        def recur(nums):
            if len(nums)<=2:
                return 1
            left = [e for e in nums if e<nums[0]]
            right = [e for e in nums if e>nums[0]]
            return comb(len(nums)-1,len(left))*recur(left)*recur(right)
        ans = (recur(nums) -1)%mod
        return ans
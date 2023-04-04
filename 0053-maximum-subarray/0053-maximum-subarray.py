class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1,ans=0,-1e6
        for i in range(len(nums)):
            sum1+=nums[i]
            sum1 = max(sum1,nums[i])
            ans = max(sum1,ans)
        return ans
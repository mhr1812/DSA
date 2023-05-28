class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for i in range(n)]
        curr = 1
        for i in range(n):
            ans[i]*=curr
            curr*=nums[i]
        curr = 1
        for i in reversed(range(n)):
            ans[i]*=curr
            curr *= nums[i]
        return ans
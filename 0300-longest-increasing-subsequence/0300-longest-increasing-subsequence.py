class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [nums[0]]
        
        for i in range(n):
            if nums[i]>ans[-1]:
                ans.append(nums[i])
            else:
                ans[bisect_left(ans,nums[i])] = nums[i] 
        return len(ans)
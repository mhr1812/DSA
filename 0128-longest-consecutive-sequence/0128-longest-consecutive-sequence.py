class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans,n = 0,len(nums)
        s = set(nums)
        for i in range(n):
            if nums[i]-1 not in s:
                j = nums[i]
                while j in s:
                    j+=1
                ans = max(ans,j-nums[i])
        return ans
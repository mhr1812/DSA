class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans,f,n = 0,0,len(nums)
        for i in range(n):
            if nums[i]>threshold:
                f=0
            elif f and nums[i-1]%2!=nums[i]%2:
                f+=1
            else:
                f = 1-nums[i]%2
            ans = max(ans,f)
                    
        return ans
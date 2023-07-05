class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left,zeros,ans,n = 0,0,0,len(nums)
        for i in range(n):
            if nums[i]==0:
                zeros+=1
            while zeros>1:
                if nums[left]==0:
                    zeros-=1
                left+=1
            ans = max(ans,i-left+1-zeros)
        return ans if ans!=n else ans-1
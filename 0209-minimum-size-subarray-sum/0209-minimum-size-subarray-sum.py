class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n,prev,ans = len(nums),0,float('inf')
        for i in range(n):
            target-=nums[i]
            while target<=0:
                ans = min(ans,i-prev+1)
                target+=nums[prev]
                prev+=1
        if ans==float('inf'):
            return 0
        else:
            return ans
                
            
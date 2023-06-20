class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1 for i in range(n)]
        size = 2*k+1
        l,sm = 0,sum(nums[:2*k])
        for i in range(2*k,n):
            sm+=nums[i]
            if i-l+1 == size:
                ans[l+k] = sm//size
                sm-=nums[l]
                l+=1 
        return ans
                
        
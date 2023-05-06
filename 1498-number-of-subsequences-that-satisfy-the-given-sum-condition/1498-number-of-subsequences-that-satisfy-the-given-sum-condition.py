m = int(1e9+7)
class Solution:
    
        
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low,high = 0,n-1
        nums.sort()
        ans = 0
        # def power(a,b):
        #     if b==0:
        #         return 1
        #     if b==1:
        #         return a
        #     ans = 0
        #     if b%2==0:
        #         ans = power(a,b//2)
        #         ans*=ans
        #     else:
        #         ans = power(a,b-1)
        #         ans*=a
        #     return ans%m
        while low<=high:
            if nums[low]+nums[high]<=target:
                ans+=1<<(high-low)
                ans%=m
                low+=1
            else:
                high-=1
        return ans%m
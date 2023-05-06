m = int(1e9+7)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low,high = 0,n-1
        nums.sort()
        ans = 0
        while low<=high:
            if nums[low]+nums[high]<=target:
                ans+=pow(2,high-low)%m
                ans%=m
                low+=1
            else:
                high-=1
        return ans%m
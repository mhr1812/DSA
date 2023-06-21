class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def calc(l):
            sm = 0
            for i,x in enumerate(nums):
                sm +=abs(l-x)*cost[i]
            return sm 
        l = min(nums)
        r = max(nums) + 1
        mid = (l+r)//2
        
        while l<r:
            if calc(mid)<calc(mid+1):
                r = mid
            else:
                l = mid+1
            mid = (l+r)//2
        
        return calc(l)
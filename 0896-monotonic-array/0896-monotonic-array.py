class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        c1=c2=1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                c1=0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                c2=0
        return c1 or c2
                
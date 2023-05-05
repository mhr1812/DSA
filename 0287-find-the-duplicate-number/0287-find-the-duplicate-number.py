class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        st = set()
        for i in range(n):
            if nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
            else:
                return abs(nums[i])
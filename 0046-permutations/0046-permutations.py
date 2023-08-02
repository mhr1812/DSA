class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        if len(nums)==0:
            return []
        def helper(nums,i):
            if i==len(nums)-1:
                permutations.append(nums.copy())
                return
            for j in range(i,len(nums)):
                nums[i],nums[j] = nums[j],nums[i]
                helper(nums,i+1)
                nums[i],nums[j] = nums[j],nums[i]
        helper(nums,0)
        return permutations
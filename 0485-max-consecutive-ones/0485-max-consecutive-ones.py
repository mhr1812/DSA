class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans,c = 0,0
        for i in range(len(nums)):
            if nums[i] == 1:
                c+=1
            else:
                c = 0
            ans = max(ans,c)
        return ans
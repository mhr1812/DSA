class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        nums.sort(reverse = True)
        i = 0
        sum1 = 0
        for i in range(n):
            sum1+=nums[i]
            if sum1>0:
                ans+=1
            else:
                break
    
        return ans
        
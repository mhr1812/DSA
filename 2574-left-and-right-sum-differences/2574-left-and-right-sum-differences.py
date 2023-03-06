class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        def leftsum(i):
            lsum = 0
            for j in range(i):
                lsum+=nums[j]
            return lsum
        def rightsum(i):
            rsum = 0
            n = len(nums)
            for j in range(i+1,n):
                rsum+=nums[j]
            return rsum
        
        ans = []
        n = len(nums)
        for i in range(n):
            ans.append(abs(leftsum(i)-rightsum(i)))
        
        return ans
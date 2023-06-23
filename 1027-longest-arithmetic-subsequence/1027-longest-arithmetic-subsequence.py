class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        t = [{} for i in range(n)]
        if n==2:
            return 2
        ans = 2
        for i in range(n):
            for j in range(i):
                d = nums[i]-nums[j]
                t[i][d] = t[j].get(d,1)+1
                ans = max(ans,t[i][d])
        return ans
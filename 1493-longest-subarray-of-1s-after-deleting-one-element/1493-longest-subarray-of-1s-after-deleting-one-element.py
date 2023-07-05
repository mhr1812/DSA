class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev,curr,ans = None,0,0
        for e in nums:
            if e:
                curr+=1
            else:
                if prev is None:
                    prev = 0
                ans = max(ans,prev+curr)
                prev = curr
                curr = 0
        if prev is None:
            return curr-1
        else:
            return max(ans,prev+curr)
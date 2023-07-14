class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = float('-inf')
        t = {}
        for i in range(len(arr)):
            if arr[i]-difference in t:
                t[arr[i]] = t[arr[i]-difference]+1
            else:
                t[arr[i]] = 1
            ans = max(ans,t[arr[i]])
        return ans
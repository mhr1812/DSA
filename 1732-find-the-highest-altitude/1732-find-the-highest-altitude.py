class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans,sm = 0,0
        for e in gain:
            sm+=e
            ans = max(ans,sm)
        return ans
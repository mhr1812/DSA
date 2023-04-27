class Solution:
    def bulbSwitch(self, n: int) -> int:
        l = 1
        r = n
        ans = 0
        while l<=r:
            mid = (l+r)//2
            sq = mid*mid
            
            if sq==n:
                return mid
            elif sq<n:
                l = mid+1
                ans = mid
            else:
                r = mid-1
        return ans
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        a = []
        for i in range(len(s)):
            if s[i] in chars:
                a.append(vals[chars.index(s[i])])
            else:
                a.append(ord(s[i])-96)
        sum1,ans = 0,-1
        for i in range(len(s)):
            sum1+=a[i]
            sum1 = max(sum1,a[i])
            ans = max(ans,sum1)
        if ans<0:
            return 0
        return ans
            
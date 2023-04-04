class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        d = defaultdict(int)
        for i,j in enumerate(chars):
            d[j] = i
        sum1,ans = 0,-1
        for i in range(len(s)):
            if s[i] in d:
                sum1+=vals[d[s[i]]]
            else:
                sum1+=ord(s[i])-96
            if sum1<0:
                sum1 = 0
            ans = max(ans,sum1)
        return ans
            
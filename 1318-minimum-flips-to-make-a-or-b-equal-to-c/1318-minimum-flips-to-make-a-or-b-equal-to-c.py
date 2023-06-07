class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(31):
            if (c>>i) & 1:
                ans+=(a>>i)&1==0 and (b>>i)&1==0
            else:
                ans+=((a>>i)&1)+((b>>i)&1)
        return ans
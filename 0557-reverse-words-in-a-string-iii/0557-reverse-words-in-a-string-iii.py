class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        ans = ""
        for e in a:
            ans+=e[::-1]
            ans+=" "
        return ans[:-1]
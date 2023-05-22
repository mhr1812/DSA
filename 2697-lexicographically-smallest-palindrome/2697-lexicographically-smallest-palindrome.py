class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in range(n//2):
            if s[i]!=s[n-i-1]:
                if ord(s[i])<ord(s[n-i-1]):
                    s = s[:n-i-1]+s[i]+s[n-i:]
                else:
                    s = s[:i] + s[n-i-1]+s[i+1:]
        return s
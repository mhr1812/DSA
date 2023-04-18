class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m = len(word1),len(word2)
        ans = ""
        if m<=n:
            for i in range(m):
                ans+=word1[i]
                ans+=word2[i]
            for i in range(m,n):
                ans+=word1[i]
        else:
            for i in range(n):
                ans+=word1[i]
                ans+=word2[i]
            for i in range(n,m):
                ans+=word2[i]
        return ans
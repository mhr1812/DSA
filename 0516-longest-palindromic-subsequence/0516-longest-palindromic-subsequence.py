class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        t = [[0 for j in range(n)]for i in range(n)]
        
        for i in range(n-1,-1,-1):
            t[i][i] = 1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    t[i][j] = 2+t[i+1][j-1]
                else:
                    t[i][j] = max(t[i+1][j],t[i][j-1])
        return t[0][n-1]
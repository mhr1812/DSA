class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        
        l,start = 1,0
        
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = 1
                l = 2
                start = i
        
        for k in range(3,n+1):
            for i in range(n-k+1):
                j = i+k-1
                if dp[i+1][j-1] and s[i]==s[j]:
                    dp[i][j] = 1
                    
                    if k>l:
                        start = i
                        l = k
        
        return s[start:start+l]
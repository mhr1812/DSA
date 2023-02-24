class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        c = [[0 for i in range(n+1)] for j in range(m+1)]
                
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                #if i==0 or j==0:
                    #c[i][j] = 0
                    
                if text1[i-1]!=text2[j-1]:
                    c[i][j] = max(c[i][j-1],c[i-1][j])
                    
                if text1[i-1]==text2[j-1]:
                    c[i][j] = c[i-1][j-1]+1
        
        return c[m][n]
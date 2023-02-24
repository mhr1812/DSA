class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        c,n = 0,len(s)
        
        for i in range(n):
            
            #odd length palindrome
            l,r = i,i
            while l>=0 and r<n and s[l] == s[r]:
                if c<r-l+1:
                    c = r-l+1
                    ans = s[l:r+1]
                l-=1
                r+=1
            
            #even length palindrome
            l,r = i,i+1
            while l>=0 and r<n and s[l] == s[r]:
                if c<r-l+1:
                    c = r-l+1
                    ans = s[l:r+1]
                l-=1
                r+=1
        
        return ans
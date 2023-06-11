class Solution:
    def smallestString(self, s: str) -> str:
        start,end,n = 0,0,len(s)
        for i in range(n):
            if s[i]=='a':
                start+=1
            else:
                break
        
        ans = list(s)
        if start==n:
            ans[-1] = 'z'
        for i in range(start,n):
            if s[i]!='a':
                ans[i] = chr(ord(ans[i])-1)
            else:
                break
            
        return ''.join(ans)
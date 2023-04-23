mod = int(1e9+7)
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        t = [-1 for i in range(n)]
        def recur(s,k,i):
            if i==n:
                return 1
            if s[i]=='0':
                return 0
            if t[i]!=-1:
                return t[i]
            ans,num = 0,0
            for j in range(i,n):
                num = 10*num + int(s[j]) 
                if num>k:
                    break
                ans=(ans+recur(s,k,j+1))%mod
            t[i] = ans
            return ans
        
        return recur(s,k,0)
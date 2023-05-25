class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0:
            return 1.0 
        if n>=k+maxPts:
            return 1.0
        
        sm,ans = 1.0,0.0
        t = [0.0 for i in range(n+1)]
        t[0] = 1.0
        
        for i in range(1,n+1):
            t[i] = sm/maxPts
            
            if i<k:
                sm+=t[i]
            else:
                ans+=t[i]
            
            if i>=maxPts:
                sm-=t[i-maxPts]
        return ans
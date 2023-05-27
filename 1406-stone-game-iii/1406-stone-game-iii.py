class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # t = {}
#         def dfs(i):
#             if i==n:
#                 return 0
#             if i in t:
#                 return t[i]
#             ans = float('-inf')
#             sm = 0
#             for j in range(i,min(n,i+3)):
#                 sm+=stoneValue[j]
#                 ans = max(ans,sm-dfs(j+1))
#             t[i] = ans
#             return ans 
#         return "Alice" if dfs(0)>0 else("Bob" if dfs(0)<0 else "Tie")

        mn = float('-inf')
        t = [0 for i in range(n+1)]
        for i in range(n-1,-1,-1):
            ans = mn
            ans = max(ans,stoneValue[i]-t[i+1])
            
            if i+1<n:
                ans = max(ans,stoneValue[i]+stoneValue[i+1]-t[i+2])
            
            if i+2<n:
                ans = max(ans,stoneValue[i]+stoneValue[i+1]+stoneValue[i+2]-t[i+3])
                
            t[i] = ans
        return "Alice" if t[0]>0 else("Bob" if t[0]<0 else "Tie")
    
        
            
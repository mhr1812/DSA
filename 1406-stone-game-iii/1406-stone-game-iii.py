class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        t = {}
        def dfs(i):
            if i==n:
                return 0
            if i in t:
                return t[i]
            ans = float('-inf')
            sm = 0
            for j in range(i,min(n,i+3)):
                sm+=stoneValue[j]
                ans = max(ans,sm-dfs(j+1))
            t[i] = ans
            return ans 
        return "Alice" if dfs(0)>0 else("Bob" if dfs(0)<0 else "Tie")
            
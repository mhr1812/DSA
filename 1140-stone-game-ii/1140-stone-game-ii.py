class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        t = {}
        def dfs(alice,i,M):
            if i==len(piles):
                return 0 
            if (alice,i,M) in t:
                return t[(alice,i,M)]
            
            ans = 0 if alice else float('inf')
            sm = 0
            for x in range(1,2*M+1):
                if i+x-1==len(piles):
                    break
                sm+=piles[i+x-1]
                if alice:
                    ans = max(ans,sm+dfs(not alice,i+x,max(M,x)))
                else:
                    ans = min(ans,dfs(not alice,i+x,max(M,x)))
            t[(alice,i,M)] = ans
             
            return ans
        
        return dfs(True,0,1)
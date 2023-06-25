class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = int(1e9+7)
        ans = 0
        
        @lru_cache(None)
        def memo(curr,left):
            if left<0:
                return 0
            
            if curr==finish:
                ans = 1
            else:
                ans = 0
            
            for nxt in range(len(locations)):
                if curr!=nxt:
                    cost = abs(locations[curr]-locations[nxt])
                    ans += memo(nxt,left-cost)
            return ans%mod 
        
        return memo(start,fuel) 
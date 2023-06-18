class Solution:    
    def countPaths(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        mod = 10**9+7
        
        @lru_cache(None)
        def recur(i,j):
            c = 1
            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=x<n and 0<=y<m and grid[x][y]>grid[i][j]:
                    c+=recur(x,y)%mod
            return c
        
        a = []
        for i in range(n):
            for j in range(m):
                a.append(recur(i,j))
        ans = sum(a)%mod
        return ans
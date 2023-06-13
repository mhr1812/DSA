class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cpy = [[0 for j in range(n)]for i in range(n)]
        for i in range(n):
            for j in range(n):
                cpy[i][j] = grid[j][i]
        ans = 0
        for e in grid:
            for f in cpy:
                if e==f:
                    ans+=1 
        return ans
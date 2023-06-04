class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                s1, s2 = set(), set()
                x1, y1 = i+1, j+1
                while x1 < m and y1 < n:
                    s1.add(grid[x1][y1])
                    x1+=1
                    y1+=1
                x2, y2 = i-1, j-1
                while x2 >= 0 and y2 >= 0:
                    s2.add(grid[x2][y2])
                    x2-=1
                    y2-=1
                ans[i][j] = abs(len(s1)-len(s2))
        return ans
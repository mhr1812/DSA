class UnionFind:

    def __init__(self, n):
        self.root = list(range(n))
        self.size = [1] * n
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_lil, root_big = self.find(x), self.find(y)
        if self.size[root_lil] > self.size[root_big]:
            root_lil, root_big = root_big, root_lil
        self.root[root_lil] = root_big
        self.size[root_big] = self.size[root_lil]


class Solution:

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        dsu = UnionFind(row * col + 2)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        grid = [[0] * col for _ in range(row)]

        for i, (r, c) in enumerate(cells):
            r, c = r - 1, c - 1
            dsu_index = r * col + c + 1
            grid[r][c] = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc]:
                    dsu.union(dsu_index, nr * col + nc + 1)
                
            if c == 0:
                dsu.union(dsu_index, 0)
            
            if c == col - 1:
                dsu.union(dsu_index, row * col + 1)
            
            if dsu.find(0) == dsu.find(row * col + 1):
                return i
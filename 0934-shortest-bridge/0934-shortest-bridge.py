class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def invalid(r,c):
            return r<0 or r==n or c<0 or c==n
        
        direct = [[0,1],[0,-1],[1,0],[-1,0]]
        
        visited = set()
        
        def dfs(r,c):
            if invalid(r,c) or not grid[r][c] or (r,c) in visited:
                return 
            visited.add((r,c))
            for e in direct:
                dfs(r+e[0],c+e[1])
        
        def bfs():
            ans = 0
            q = deque(visited)
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for e in direct:
                        r1 = r+e[0]
                        c1 = c+e[1]
                        if invalid(r1,c1) or (r1,c1) in visited:
                            continue
                        if grid[r1][c1]:
                            return ans
                        q.append([r1,c1])
                        visited.add((r1,c1))
                ans+=1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs()
                
            
        
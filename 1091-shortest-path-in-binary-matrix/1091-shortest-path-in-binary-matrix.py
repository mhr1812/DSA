from queue import Queue
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        n = len(grid)
        q = Queue()
        dx = [-1,0,1]
        dy = [-1,0,1]
        q.put([0,0,1])
        grid[0][0] = 1
        
        while not q.empty():
            x,y,ans = q.get()
            if x==n-1 and y==n-1:
                return ans
            
            for i in range(3):
                for j in range(3):
                    nx = x+dx[i]
                    ny = y+dy[j]
                    
                    if 0<=nx<=n-1 and 0<=ny<=n-1 and grid[nx][ny]==0:
                        q.put([nx,ny,ans+1])
                        grid[nx][ny] = 1
        return -1
                
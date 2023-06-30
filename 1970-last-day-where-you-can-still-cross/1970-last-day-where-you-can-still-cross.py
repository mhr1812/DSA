class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def bfs(day):
            arr = [[0 for j in range(col)]for i in range(row)]
            dr = [[1,0],[-1,0],[0,1],[0,-1]]
            q = deque()
            for i in range(day):
                arr[cells[i][0]-1][cells[i][1]-1] = 1
            for j in range(col):
                if arr[0][j]==0:
                    q.append([0,j])
                    arr[0][j] = -1
            while q:
                r,c = q.popleft()
                if r==row-1:
                    return True
                for x1,y1 in dr:
                    if 0<=r+x1<row and 0<=c+y1<col and arr[r+x1][c+y1]==0:
                        q.append([r+x1,c+y1])
                        arr[r+x1][c+y1]=-1
            return False
            
            
        left,right = 1, row*col
        while left<right:
            mid = right - (right - left) // 2
            if bfs(mid):
                left = mid
            else:
                right = mid-1
        return left
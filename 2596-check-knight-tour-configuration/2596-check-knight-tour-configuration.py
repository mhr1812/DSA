class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        def linearSearch (arr, target):
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if (arr[i][j] == target):
                        return [i, j]
        if grid[0][0]!=0:
            return False
        
        for i in range(1,n**2):
            ans1 = linearSearch(grid,i-1)
            ans2 = linearSearch(grid,i)
            if (abs(ans1[0]-ans2[0])==2 and abs(ans1[1]-ans2[1])==1) or (abs(ans1[0]-ans2[0])==1 and abs(ans1[1]-ans2[1])==2):
                continue
            else:
                return False
        return True
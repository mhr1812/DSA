class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        N = len(matrix[0])
        M = len(matrix)
        def binarysearch(row):
            l,r = 0,N-1

            while l<=r:
                mid = (l+r)//2
                if matrix[row][mid]==target:
                    return True
                elif matrix[row][mid]<target:
                    l = mid+1
                else:
                    r = mid-1
            return False
        
        for row in range(M):
            if binarysearch(row): return True
        return False
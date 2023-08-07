class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up,down = 0,len(matrix)-1
        row = -1
        while up<=down:
            mid = up + (down-up)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                row = mid
                break
            elif target<=matrix[mid][0]:
                down = mid-1
            else:
                up = mid+1
        l,r = 0,len(matrix[0])-1
        while l<=r:
            mid = l+(r-l)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                r = mid-1
            else:
                l = mid+1
        return False
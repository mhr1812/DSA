class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) -1
        while left <= right:
            mid = (right + left) // 2

            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid 
            elif arr[mid+1] > arr[mid]:
                #+1 greater need to go to the right since larger arr there 
                left = mid + 1
            else:
                #-1 greater need to go to the left since larger arr there
                right = mid - 1
        
        return right
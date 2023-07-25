class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while(left < right):
            middle = (left + right)//2

            if arr[middle - 1] < arr[middle] and arr[middle + 1] < arr[middle]:
                return middle
            
            if arr[middle + 1] > arr[middle] and arr[middle -1] < arr[middle]:
                left = middle
            
            if arr[middle + 1] < arr[middle] and arr[middle] < arr[middle -1]:
                right = middle
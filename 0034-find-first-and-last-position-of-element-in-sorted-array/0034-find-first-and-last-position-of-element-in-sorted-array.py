class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums,target):
            l=0
            h=len(nums)-1
            while l<=h:
                m=(l+h)//2
                
                if nums[m]<target:
                    l=m+1
                else:
                    h=m-1
            
            return [l,h]
        left = binarySearch(nums,target-0.1)
        right=binarySearch(nums,target+0.1)
        if left[0]!=right[0]:
            return[left[0],right[1]]
        return [-1,-1]
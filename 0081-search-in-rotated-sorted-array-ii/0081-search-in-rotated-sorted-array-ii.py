class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n==0:
            return False
        if n==1:
            return nums[0] == target
        if n==2:
            return nums[0] == target or nums[1] == target
        
        m = n//2
        if nums[m] == target:
            return True
        
        if nums[0] < nums[m]:
            if nums[m]>target and nums[0]<=target:
                return self.search(nums[:m],target)
            else:
                return self.search(nums[m+1:],target)
        elif nums[0] > nums[m]:
            if nums[m]<target and nums[n-1]>=target:
                return self.search(nums[m+1:],target)
            else:
                return self.search(nums[:m],target)
        else:
            i=1
            while True:
                if nums[i]!=nums[0]:
                    return self.search(nums[i:m],target)
                if nums[m+i]!=nums[m]:
                    return self.search(nums[m+i:],target)
                if i==m:
                    return False
                i+=1
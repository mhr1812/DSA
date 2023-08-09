class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        mini_max_diff = 0
        maxi_max_diff = nums[-1]-nums[0]
        
        while mini_max_diff<=maxi_max_diff:
            mid = (mini_max_diff+maxi_max_diff)//2
            c,i = 0,1
            
            while i<n:
                if nums[i]-nums[i-1]<=mid:
                    c+=1
                    i+=1
                i+=1
            
            if c>=p:
                maxi_max_diff = mid-1
            else:
                mini_max_diff = mid+1
            
        return mini_max_diff
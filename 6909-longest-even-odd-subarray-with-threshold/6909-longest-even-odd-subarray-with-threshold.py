class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans,curr,n = 0,1,len(nums)
        if n==0:
            return n
        for i in range(n):
            if nums[i]%2==0 and ans==0 and nums[i]<=threshold:
                ans = 1
            if nums[i]%2==0 and nums[i]<=threshold:
                for j in range(i+1,n):
                    if nums[j]%2!=nums[j-1]%2 and nums[j]<=threshold:
                        curr+=1
                        ans = max(ans,curr)
                    else:
                        break
            curr = 1
                    
        return ans
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_val = nums[k]
        l = k
        r = k
        ret = 0
        while l>=0 or r<n:
            # print("minva", min_ val)
            while l>=0 and nums[l] >= min_val:
                l-=1
            while r<n and nums[r]>= min_val:
                r+=1
            ret = max(ret, (r-l+1-2)*min_val)
            min_val = max(nums[l] if l>=0 else 0, nums[r] if r<n else 0)
        return ret
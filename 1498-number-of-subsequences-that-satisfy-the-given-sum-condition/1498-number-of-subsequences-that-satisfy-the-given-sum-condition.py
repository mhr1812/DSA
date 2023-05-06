m = int(1e9+7)
class Solution:
    
        
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        total_cnts = 0
        l, r = 0, len(nums) - 1

        while l <= r and nums[l] <= target:
            r = bisect_right(nums, target - nums[l], l, r + 1) - 1  # binary find end limit
            if r < l: break  # end limit can not be found after start

            # any subsequences starts from i and ends before j+1 will be valid
            # so, it's like choose 01 bits from the rest possitions except start
            total_cnts += 1 << r - l
            l += 1

        return total_cnts%m
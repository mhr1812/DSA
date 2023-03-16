class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapify(nums)
        
        res = 0
        for i in range(k):
            t = -heappop(nums)
            res += t
            heappush(nums, -ceil(t / 3))
        
        return res
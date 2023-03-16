class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        for i in range(k):
            t = nums.pop()
            ans += t
            x = ceil(t/3)
            nums.insert(bisect.bisect(nums,x),x)
        return ans
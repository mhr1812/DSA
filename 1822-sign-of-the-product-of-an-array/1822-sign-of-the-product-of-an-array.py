class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return 0 if 0 in nums else reduce(mul, [-1 if num < 0 else 1 for num in nums])
        
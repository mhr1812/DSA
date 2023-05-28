class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        full_product = 1
        for idx, i in enumerate(nums):
            if i == 0:
                zeroes += 1
                if zeroes > 1:
                    return [0] * len(nums)
                position = idx
            else:
                full_product *= i
        if zeroes:
            result = [0] * len(nums)
            result[position] = full_product
        else:
            result = [full_product//i for i in nums]
                
        return result
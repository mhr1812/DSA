class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        for e in nums:
            if e%2==0:
                ans.append(e)
        for e in nums:
            if e%2==1:
                ans.append(e)
        return ans
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        for i in range(len(nums)):
            if ans and ans[-1][1]==nums[i]-1:
                ans[-1][1] = nums[i]
            else:
                ans.append([nums[i],nums[i]])
        return [f'{x}->{y}' if x!=y else f'{x}' for x,y in ans]
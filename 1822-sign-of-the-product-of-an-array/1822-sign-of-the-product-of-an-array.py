class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg,f = 0,0
        for i in range(len(nums)):
            if nums[i]<0:
                neg+=1
            if nums[i]==0:
                f=1
                break
        if f:
            return 0
        elif neg%2==1:
            return -1
        else:
            return 1
        
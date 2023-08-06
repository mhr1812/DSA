class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        nums = set(nums) 

        # while there are elements in the set
        while nums:

            # check values around the popped value
            left = right = nums.pop() # O(1)

            # get sequence length before the popped value
            while left - 1 in nums: # O(1)
                left -= 1
                nums.remove(left) # O(1)
            
            # get sequence length after the popped value
            while right + 1 in nums: # O(1)
                right += 1
                nums.remove(right) # O(1)

            # update the sequence length if it is better than our best sequence length
            if right-left+1 > best: 
                best = right-left+1

        return best
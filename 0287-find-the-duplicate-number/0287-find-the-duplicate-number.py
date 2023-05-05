class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        st = set()
        for i in range(n):
            if nums[i] not in st:
                st.add(nums[i])
            else:
                return nums[i]
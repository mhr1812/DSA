class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans0,ans1 = [],[]
        nums1,nums2 = set(nums1),set(nums2)
        for e in nums1:
            if e not in nums2:
                ans0.append(e)
        for e in nums2:
            if e not in nums1:
                ans1.append(e)
        return [ans0,ans1]
            
        
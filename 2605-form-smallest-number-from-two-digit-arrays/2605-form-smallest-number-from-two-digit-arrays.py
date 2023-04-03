class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        nums1.sort()
        nums2.sort()
        nums = nums1+nums2
        c = Counter(nums)
        d = sorted(c.items(),key = lambda x:x[1], reverse=True)
        if d[0][1]>1:
            return d[0][0]
        else:
            return int(str(min(nums1[0],nums2[0]))+str(max(nums1[0],nums2[0])))
        
            
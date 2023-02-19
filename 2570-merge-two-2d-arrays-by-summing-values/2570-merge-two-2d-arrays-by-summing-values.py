class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n,m = len(nums1),len(nums2)
        ans = []
        for i in range(n):
            #if nums1[i][0] in (x[0] for x in nums2):
            for j in range(m):
                if nums1[i][0]==nums2[j][0]:
                    nums1[i][1] += nums2[j][1]
            ans.append(nums1[i])
        for k in range(m):
            if nums2[k][0] not in (x[0] for x in nums1):
                ans.append(nums2[k])
        ans.sort(key=lambda x:x[0])        
        return ans
        
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans,prefixSum, x = -1,0,[]
        pairs = zip(nums1,nums2)
        pairs = sorted(pairs,key = lambda x:x[1],reverse=True)
        
        for e in pairs:
            prefixSum+=e[0]
            heappush(x,e[0])
            if len(x)==k:
                ans = max(ans,prefixSum*e[1])
                prefixSum-=heappop(x)
        return ans
        
        
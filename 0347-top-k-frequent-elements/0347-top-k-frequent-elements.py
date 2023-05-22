class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        a = sorted(c.items(),reverse=True,key = lambda x:x[1])
        ans = []
        for i in range(k):
            ans.append(a[i][0])
        return ans
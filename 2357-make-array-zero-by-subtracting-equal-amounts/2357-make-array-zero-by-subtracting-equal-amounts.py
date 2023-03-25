class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for e in nums:
            if e!=0:
                d[e]+=1
        return len(d)
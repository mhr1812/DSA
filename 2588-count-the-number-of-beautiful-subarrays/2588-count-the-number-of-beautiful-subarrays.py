class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter({0:1})
        for val in accumulate(nums,operator.xor):
            cnt[val]+=1
        return sum(v*(v-1)//2 for v in cnt.values()) 
        
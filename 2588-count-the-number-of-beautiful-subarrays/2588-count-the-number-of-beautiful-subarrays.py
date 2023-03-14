class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        pre_xor = [0 for i in range(n+1)]
        count = [0 for i in range(1<<20)]
        ans = 0
        count[0] = 1
        for i in range(1,n+1):
            pre_xor[i] = pre_xor[i-1]^nums[i-1]
            ans+=count[pre_xor[i]]
            count[pre_xor[i]]+=1
        return ans
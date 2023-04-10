class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = [0 for i in range(n)]
        c = Counter(nums)  
        d = {}    
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                d[nums[i]] += i
        for i in range(n):
            a[i] = d[nums[i]]-c[nums[i]]*i
            d[nums[i]]-=2*i
            c[nums[i]]-=2
        return a
                
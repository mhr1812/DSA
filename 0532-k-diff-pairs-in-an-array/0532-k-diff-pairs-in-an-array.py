class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        c = Counter(nums)
        
        if k==0:
            for key,val in c.items():
                if val>1:
                    ans+=1
        else:
            for key,val in c.items():
                if key+k in c:
                    ans+=1
        return ans
            
class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        while n:
            k = 1
            while pow(2,k)<n:
                k+=1
            n = min(pow(2,k)-n,n-pow(2,k-1))
            ans+=1
        return ans
        
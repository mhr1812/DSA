mod = pow(10,9)+7
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        t = Counter({0:1})
        
        for i in range(1,high+1):
            t[i] = (t[i-zero] + t[i-one]) % mod
        return sum(t[i] for i in range(low,high+1)) % mod
    
        
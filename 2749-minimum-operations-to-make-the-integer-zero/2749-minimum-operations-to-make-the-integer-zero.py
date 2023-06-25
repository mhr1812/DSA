class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        def countSetBits(n):
            n = bin(n)
            return n.count("1")
        
        for i in range(101):
            val = num1 - i*num2
            if countSetBits(val)<=i and i<=val:
                return i
        
        return -1
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        def countSetBits(n):
            n = bin(n)
            return n.count("1")
        
        for i in range(101):
            val = num1 - i*num2
            if val<i or countSetBits(val)>i:
                continue
            return i
        
        return -1
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        while a or b or c:
            abit = a & 1
            bbit = b & 1
            cbit = c & 1

            if abit | bbit != cbit:
                if abit & bbit & ~cbit:
                    flips += 2
                else:
                    flips += 1        

            a >>= 1
            b >>= 1
            c >>= 1

        return flips
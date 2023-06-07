class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        for i in range(31):
            mask = 1 << i
            if (c & mask) == 0:
                if (a & mask) > 0:
                    count += 1
                if (b & mask) > 0:
                    count += 1
            else:
                if (a & mask) == 0 and (b & mask) == 0:
                    count += 1
        return count

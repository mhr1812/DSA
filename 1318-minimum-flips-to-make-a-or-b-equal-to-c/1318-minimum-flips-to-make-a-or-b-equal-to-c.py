class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        d = (a|b)^c
        return d.bit_count() + (a & b & d).bit_count()
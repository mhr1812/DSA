class Solution:
    def maxRunTime(self, n: int, a: List[int]) -> int:
        if len(a) < n:
            return 0
        if len(a) == n:
            return min(a)
        
        s = sum(a)
        if n == 1:
            return sum(a)
        
        t = s // n
        if t >= max(a):
            return t

        m = len(a)
        a = sorted(Counter(a).items())
        p = m
        q = s
        for i, j in a[::-1]:
            p -= j
            q -= i * j
            if q + i * (m - p) >= i * n:
                return (q + i * j) // (n - m + p + j)
        return 0       
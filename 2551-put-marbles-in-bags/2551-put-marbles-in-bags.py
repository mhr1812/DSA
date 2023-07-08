class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        a = []
        for i in range(n-1):
            a.append(weights[i]+weights[i+1])
        a.sort()
        return sum(a[n-k:])-sum(a[:k-1])
        
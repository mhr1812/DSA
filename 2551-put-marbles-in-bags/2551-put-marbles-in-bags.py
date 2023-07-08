class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        a = [x+y for x,y in pairwise(weights)]
        if k==1:
            return 0
        a.sort()
        k-=1
        return sum(a[-k:])-sum(a[:k])
        
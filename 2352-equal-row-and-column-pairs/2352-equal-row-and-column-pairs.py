class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        for e in grid:
            d[tuple(e)] +=1
        ans = 0
        for e in zip(*grid):
            ans+=d[tuple(e)]
        return ans
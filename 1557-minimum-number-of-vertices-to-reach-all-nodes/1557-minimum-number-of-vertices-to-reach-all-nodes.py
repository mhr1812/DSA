class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        for e in edges:
            d[e[1]] = 1
        ans = set()
        for e in edges:
            if not d[e[0]]:
                ans.add(e[0])
        return list(ans)
class DSU(object):
    def __init__(self, n):
        self.parents = [i for i in range(n)]
    
    def find(self,x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        rootA, rootB = self.find(x), self.find(y)
        if rootA != rootB:
            self.parents[rootA] = rootB
            
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        for i, q in enumerate(queries):
            queries[i].append(i)

        queries.sort(key=lambda q: q[2])
        edgeList.sort(key=lambda e: e[2])

        i = 0
        res = [False] * len(queries)
        for q in queries:
            while i < len(edgeList) and edgeList[i][2] < q[2]:
                dsu.union(edgeList[i][0], edgeList[i][1])
                i += 1

            if dsu.find(q[0]) == dsu.find(q[1]):
                res[q[3]] = True

        return res

        
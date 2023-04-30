def find(reps, u):
    if reps[u] == -1:
        return u
    reps[u] = find(reps, reps[u])
    return reps[u]

def union(reps, u, v):
    rep_u = find(reps, u)
    rep_v = find(reps, v)
    if rep_u != rep_v:
        reps[rep_u] = rep_v

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        m3 = 0 # number of type 3 edges added
        reps = [-1] * (n + 1)
        for t, u, v in edges:
            if t == 3 and find(reps, u) != find(reps, v):
                union(reps, u, v)
                m3 += 1
        
        m1 = 0 # number of type 1 edges added
        m2 = 0 # number of type 2 edges added
        reps2 = reps.copy()
        for t, u, v in edges:
            if t == 1 and find(reps, u) != find(reps, v):
                union(reps, u, v)
                m1 += 1
            elif t == 2 and find(reps2, u) != find(reps2, v):
                union(reps2, u, v)
                m2 += 1
        
        if m1 + m3 != n - 1 or m2 + m3 != n - 1:
            return -1
        
        return len(edges) - (m1 + m2 + m3)
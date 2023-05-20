class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def bellman_ford(src, trg):
            if src == trg:
                return 1.
            
            V = len(vertices)
            dist = {v: float('inf') for v in vertices}
            dist[src] = 1.
            
            for i in range(V - 1):
                for u, v, w in edges:
                    dist[v] = min(dist[v], dist[u] * w)
            
            return dist[trg] if dist[trg] != float('inf') else -1.
        
        n = len(equations)
        vertices = set()
        edges = []
        
        for i in range(n):
            a, b = equations[i]
            val = values[i]
            
            vertices.add(a)
            vertices.add(b)
            
            edges.append((a, b, val))
            edges.append((b, a, 1 / val))
        
        res = [-1.] * len(queries)
        for i, query in enumerate(queries):
            c, d = query
            if c in vertices and d in vertices:
                res[i] = bellman_ford(c, d)
        
        return res
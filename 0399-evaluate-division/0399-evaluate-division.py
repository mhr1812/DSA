class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(dict)
        
        for (x,y),v in zip(equations,values):
            g[x][y] = v
            g[y][x] = 1/v
            
        def bfs(src,dst):
            if not(src in g and dst in g):
                return -1.0
            q = [(src,1.0)]
            visited = set()
            
            for x,v in q:
                if x==dst:
                    return v
                visited.add(x)
                for y in g[x]:
                    if y not in visited:
                        q.append((y,v*g[x][y]))
            return -1.0
        return [bfs(s,d) for s,d in queries]
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        def dfs(v,curr):
            if v in color:
                return color[v]==curr
            
            color[v] = curr
            return all(dfs(w, 1-curr) for w in graph[v])
        
        
        return all(dfs(v, 0) for v in range(len(graph)) if v not in color)
            
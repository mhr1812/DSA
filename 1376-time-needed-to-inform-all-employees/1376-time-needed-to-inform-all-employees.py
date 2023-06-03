class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            if manager[i]!=-1:
                graph[manager[i]].append(i)
        
        def dfs(node,graph):
            mx = 0
            for child in graph[node]:
                mx = max(mx,dfs(child,graph))
            return mx+informTime[node]
        
        return dfs(headID,graph)
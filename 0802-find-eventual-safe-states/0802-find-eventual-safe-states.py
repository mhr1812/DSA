class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False] * n
        unsafe = [0] * n
        
        def dfs(i):
            isSafe = True
            for neighbor in graph[i]:
                if visited[neighbor] or unsafe[neighbor] == 2:
                    isSafe = False
                    break
                if unsafe[neighbor] == 1:
                    continue
                visited[neighbor] = True
                if not dfs(neighbor):
                    isSafe = False
                visited[neighbor] = False
            unsafe[i] = 1 if isSafe else 2
            return isSafe
        
        for i in range(n):
            if unsafe[i] == 0:
                visited[i] = True
                dfs(i)
                visited[i] = False

        result = []
        for i in range(len(unsafe)):
            if unsafe[i] == 1:
                result.append(i)
        return result
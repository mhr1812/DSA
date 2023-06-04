class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ans = 0
        visited = [0 for i in range(n)]
        
        def dfs(node):
            visited[node] = 1 
            for i in range(n):
                if isConnected[node][i] and not visited[i]:
                    dfs(i)
        
        ans = 0
        for i in range(n):
            if not visited[i]:
                ans+=1
                dfs(i)
        return ans
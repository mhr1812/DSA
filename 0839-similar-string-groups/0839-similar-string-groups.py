from collections import deque
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(a,b):
            c = 0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    c+=1
            return c==2 or c==0 
    
        n = len(strs)
        graph = [[] for i in range(n)]
        
        for i in range(n):
            for j in range(i+1,n):
                if is_similar(strs[i],strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = [False for i in range(n)]
        ans = 0
        
        for i in range(n):
            if visited[i]: continue
            ans+=1
            q = deque([i])
            
            while q:
                node = q.popleft()
                if visited[node]: continue
                visited[node] = True
                
                for v in graph[node]:
                    if visited[v]: continue
                    q.append(v)
        return ans
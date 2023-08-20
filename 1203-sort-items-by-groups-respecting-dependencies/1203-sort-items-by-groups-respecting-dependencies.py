class Solution:
    def sortItems(self, n, m, group, beforeItems):
        group_id = m
        for i in range(n):
            if group[i]==-1:
                group[i] = group_id
                group_id += 1
                
        item_g = [[] for _ in range(n)]
        item_d = [0]*n
        
        g_g = [[] for _ in range(group_id)]
        g_d = [0]*group_id
        
        for i in range(n):
            for j in beforeItems[i]:
                item_g[j].append(i)
                item_d[i] += 1
                
                if group[i]!=group[j]:
                    g_g[group[j]].append(group[i])
                    g_d[group[i]] += 1
                    
        def topologicalSort(graph, indegree):
            visited = []
            q = [node for node in range(len(graph)) if indegree[node] == 0]
            while q:
                cur = q.pop()
                visited.append(cur)
                for neib in graph[cur]:
                    indegree[neib] -= 1
                    if indegree[neib] == 0:
                        q.append(neib)
            return visited if len(visited) == len(graph) else []
        
        item = topologicalSort(item_g, item_d)
        g = topologicalSort(g_g, g_d)
        #print(item, g, item_g, g_g)
        
        if not item or not g:
            return []
        
        tmp = defaultdict(list)
        for i in item:
            tmp[group[i]].append(i)
            
        ans = []
        for i in g:
            ans += tmp[i]
            
        return ans
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for pos,i in enumerate(equations):
            adj[i[0]].append((i[1],values[pos]))
            adj[i[1]].append((i[0],1/values[pos]))
            
        #  0 -> false
        #  1 -> true
        # -1 -> not found
        
        def value_f():
            return -1
        
        def createdict(visited):
            for pair in equations:
                visited[pair[0]] = 0
                visited[pair[1]] = 0
        
        output = []
        def dfs(start,END,res):
            if visited[start] == 1:
                return
            visited[start] = 1 # is Visited
            if start == END:   #reach to endpoints
                if len(adj[start]) != 0:
                    output.append(res)
                return

            for s_to in adj[start]:
                if visited[s_to[0]] == 0:
                    # print(start,"->",s_to[0],END,res * s_to[1])
                    dfs(s_to[0],END,res * s_to[1])       
                    
        for pos,pair in enumerate(queries):
            visited = defaultdict(value_f)
            createdict(visited)
            if(visited[pair[0]] == -1 or visited[pair[1]] == -1): #that point not appear in graph
                output.append(-1)
                continue
            dfs(pair[0],pair[1],1)   #traverse by DFS
            if len(output) < pos + 1: # append nothing after executing dfs() 
                output.append(-1)
            
        return output
class Solution:
    def solver(self,x,y,graph,visited):
        if x not in graph:
            return -1.0
        if x==y:
            return 1
        visited.add(x)  
        for key,val in graph[x]:
            if key not in visited:
                crnt=self.solver(key,y,graph,visited)
                if crnt!=-1:
                    return val*crnt
        return -1.0
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(set)
        for [u,v],val in zip(equations,values):
            graph[u].add((v,val))
            graph[v].add((u,1/val))
        out=[]
        for c,d in queries:
            out.append(self.solver(c,d,graph,set()))
        return out


        ans=[]
        for p,q in queries:
            ans.append(dfs(p,q,set()))

        return ans             
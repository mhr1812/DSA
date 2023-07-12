class Solution:
    def dfs(self,graph,vis,dfs_vis,cycle_ele,s):
        vis[s]=True
        dfs_vis[s]=True
        for node in graph[s]:
            if (vis[node] == False) :
                if (self.dfs(graph,vis,dfs_vis,cycle_ele,node)) :
                    cycle_ele[s] = True
                    return cycle_ele
            elif (vis[node] and dfs_vis[node]):
                cycle_ele[s]= True
                return cycle_ele
        dfs_vis[s] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans=[]
        l=len(graph)
        vis=[False]*l
        dfs_vis=[False]*l
        cycle_ele=[False]*l
        for i in range(l):
            if (vis[i] == False) :
                self.dfs(graph,vis,dfs_vis,cycle_ele,i)
        for i in range(len(cycle_ele)):
            if cycle_ele[i]== False  :
                ans.append(i)
        return ans
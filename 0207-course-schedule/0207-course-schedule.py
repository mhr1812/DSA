class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build adj_lst
        adj_list = [[] for i in range(numCourses)]
        for pre in prerequisites:
            adj_list[pre[1]].append(pre[0])

        visit = [-1 for i in range(numCourses)] # -1 not yet visit, 1 visit, 0, processing in this DFS

        def DFS(index):
            
            edges = adj_list[index]
            visit[index] = 0
            for vertex in edges:
                if visit[vertex] == 1:
                    continue
                elif visit[vertex] == -1:
                    if not DFS(vertex):
                        return False
                else:
                    return False

            visit[index] = 1
            return True

        result = True

        for i in range(len(adj_list)):

            if visit[i] == 1:
                continue
            else:
                result = DFS(i)
                if not result:
                    return False
        
        return True
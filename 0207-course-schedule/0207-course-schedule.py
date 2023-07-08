class Solution:
     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]

        for pre in prerequisites:
            a, b = tuple(pre)
            graph[b].append(a)
            indegrees[a] += 1
        
        stack = [i for i in range(numCourses) if indegrees[i] == 0]
        visited = 0

        while stack:
            node = stack.pop()
            visited += 1

            for next_node in graph[node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    stack.append(next_node)
        
        return visited == numCourses
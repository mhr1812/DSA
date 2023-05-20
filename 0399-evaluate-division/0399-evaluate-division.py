class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        parents = dict()
        def find(i):
            if i not in parents:
                parents[i] = i
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]
        graph = defaultdict(dict)
        for i in range(n):
            a,b = equations[i]
            graph[a][b] = values[i]
            graph[b][a] = 1/values[i]

            root_a = find(a); root_b = find(b)
            parents[root_b] = root_a

        def bfs(a, b):
            que = deque([[a, 1]])
            while que:
                c_node, c_res = que.popleft()
                if c_node == b:
                    return c_res
                for neigh, multiple in graph[c_node].items():
                    que.append([neigh, c_res*multiple])

        for i in range(len(queries)):
            a,b = queries[i]
            if a not in parents or b not in parents:
                queries[i] = -1
            elif find(a) != find(b):
                queries[i] = -1
            else:
                queries[i] = bfs(a, b)

        return queries
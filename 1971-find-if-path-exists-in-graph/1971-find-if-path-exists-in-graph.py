class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        queue = []
        queue.append(source)
        visited = set()
        visited.add(source)
        graph = defaultdict(set)

        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)

        while queue:
            curr = queue.pop(0)
            if curr==destination:
                return True

            for nxt in graph[curr]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        return False
            
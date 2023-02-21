class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        queue = deque()
        queue.append(source)
        visited = set()
        visited.add(source)
        graph = defaultdict(list)

        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        while queue:
            curr = queue.popleft()
            if curr==destination:
                return True

            for nxt in graph[curr]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        return False
            
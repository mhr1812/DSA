class Solution:

    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))
            self.size = [1] * size
            self.max_size = 1

        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x != root_y:
                if self.size[root_x] < self.size[root_y]:
                    root_x, root_y = root_y, root_x
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
                self.max_size = max(self.max_size, self.size[root_x])
                return True
            return False

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        sorted_edges = [edge.copy() for edge in edges]

        for i, edge in enumerate(sorted_edges):
            edge.append(i)

        sorted_edges.sort(key=lambda x: x[2])

        union_find_standard = self.UnionFind(n)
        minimum_spanning_tree_weight = 0
        for u, v, weight, _ in sorted_edges:
            if union_find_standard.union(u, v):
                minimum_spanning_tree_weight += weight

        critical_edges = []
        pseudo_critical_edges = []
        for (u, v, weight, i) in sorted_edges:
            union_find_temp = self.UnionFind(n)
            temp_weight = 0
            for (x, y, w_temp, j) in sorted_edges:
                if i != j and union_find_temp.union(x, y):
                    temp_weight += w_temp

            if union_find_temp.max_size < n or temp_weight > minimum_spanning_tree_weight:
                critical_edges.append(i)
                continue

            union_find_force = self.UnionFind(n)
            force_weight = weight
            union_find_force.union(u, v)
            for (x, y, w_force, j) in sorted_edges:
                if i != j and union_find_force.union(x, y):
                    force_weight += w_force

            if force_weight == minimum_spanning_tree_weight:
                pseudo_critical_edges.append(i)

        return [critical_edges, pseudo_critical_edges]
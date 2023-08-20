from collections import defaultdict, deque

class Solution:

    def topological_sort(self, graph, m, kaka = False):
        in_degrees = defaultdict(int)
        for key, val in graph.items():
            in_degrees[key] = 0

        for node in graph:
            for neighbor in graph[node]:
                in_degrees[neighbor] += 1
        
        zero_in_degree_queue = deque()

        topological_order = []

        for node, val in in_degrees.items():
            if val == 0:
                zero_in_degree_queue.append(node)
        while zero_in_degree_queue:
            current = zero_in_degree_queue.popleft()
            topological_order.append(current)
            for n in graph[current]:
                in_degrees[n] -=1
                if in_degrees[n] == 0:
                    zero_in_degree_queue.append(n)

        if len(topological_order) == len(graph):
            return topological_order

        # Cycle was found
        return [] 


    def make_group_graph(self, m, group_info, before_items):
        group_graph = {}
        for g in group_info:
            group_graph[g] = []

        for item, prerequisites in enumerate(before_items):
            group_of_item = group_info[item]
            for prerequisite in prerequisites:
                group_of_prereq = group_info[prerequisite]
                if group_of_item not in group_graph[group_of_prereq] and group_of_prereq != group_of_item:
                    group_graph[group_of_prereq].append(group_of_item)

        return group_graph

    def make_in_group_dependency_graph(self, elems, before_items, group_info):
        in_group_dependency_graph = {}
        for elem in elems:
            in_group_dependency_graph[elem] = []
        
        for elem in elems:
            prerequisites = before_items[elem]
            for prerequisite in prerequisites:
                if prerequisite not in elems:
                    continue
                if elem not in in_group_dependency_graph[prerequisite]:
                    in_group_dependency_graph[prerequisite].append(elem)
        
        return in_group_dependency_graph 

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        un_grouped_next = m
        ## Notice that ungrouped items DO NOT constitue a separate group.
        ## Therefore we can treat each ungrouped item as being in its own separate group.
        ## The following code replaces all -1s from the group array with new unique group IDs

        for idx, item in enumerate(group):
            if item == -1:
                group[idx] = un_grouped_next
                un_grouped_next += 1

        ## Just group all elements belonging to a particular group in a dictionary of the form {"group_id": [members]}
        for item, g in enumerate(group):
            groups[g].append(item)
        
        group_graph = self.make_group_graph(m, group, beforeItems)
        group_topological_order = self.topological_sort(group_graph, m)

        if group_topological_order == []:
            return []

        res = []
        for group in group_topological_order:
            # Make in_group_dependency_graph
            elems = groups[group]
            in_group_dependency_graph = self.make_in_group_dependency_graph(elems, beforeItems, group)
            if not elems:
                continue
    
            in_group_topological_order = self.topological_sort(in_group_dependency_graph, len(in_group_dependency_graph), True)
            if in_group_topological_order == []:
                return []
            res.extend(in_group_topological_order)

        return res
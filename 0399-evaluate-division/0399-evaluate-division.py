class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hashmap = {}
        for index, [left, right] in enumerate(equations):
            value = values[index]
            if left not in hashmap:
                hashmap[left] = [(value, right)]
            else:
                hashmap[left].append((value, right))
            if right not in hashmap:
                hashmap[right] = [(1 / value, left)]
            else:
                hashmap[right].append((1 / value, left))
		
		# BFS keep replacing x till we reach a (num, y)
        def solve(x, y):
            if x not in hashmap or y not in hashmap:
                return -1
            visited = set()
            q = deque([(1, x)])
            visited.add(x)
            while q:
                (num, var) = q.pop()
                if var == y:
                    return num
                replace_list = hashmap[var]
                for (num_2, var_2) in replace_list:
                    if var_2 not in visited:
                        visited.add(var_2)
                        q.append((num * num_2, var_2))
            return -1

        res = []
        for query in queries:
            res.append(solve(query[0], query[1]))
        return res
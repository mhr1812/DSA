class Solution:
    def maximumRequests(self, n: int, req: List[List[int]]) -> int:
        def canJoin(path, e): return req[e][0] == req[path[-1]][1]
        def cyclic(path): return req[path[0]][0] == req[path[-1]][1]
        def values(cycles): return len(sum(cycles, []))
        def overlap(p1, p2): return any([True for e in p1 if e in p2])

        def include(cycle, cycles): return [
            c for c in cycles if not overlap(c, cycle)] + [cycle]

        iter = range(len(req))

        cycles = [[e] for e in iter if req[e][0] == req[e][1]]
        paths = [[e] for e in iter]

        newPaths = []
        for i in range(2, n+1):
            for path in paths:
                for e in [e for e in iter if e not in path and canJoin(path, e)]:
                    newPath = path + [e]
                    if cyclic(newPath):
                        newCycle = include(newPath, cycles)
                        if values(newCycle) > values(cycles):
                            cycles = newCycle
                    else:
                        newPaths.append(newPath)
            paths = newPaths
            newPaths = []

        return values(cycles)
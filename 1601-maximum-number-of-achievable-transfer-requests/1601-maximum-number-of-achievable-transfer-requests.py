class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        for ans in range(m,0,-1):
            for c in combinations(range(m),ans):
                deg = [0 for i in range(n)]
                for i in c:
                    deg[requests[i][0]]-=1
                    deg[requests[i][1]]+=1
                if not any(deg):
                    return ans
        return 0
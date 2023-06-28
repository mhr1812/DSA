class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append([edges[i][1],succProb[i]])
            graph[edges[i][1]].append([edges[i][0],succProb[i]])
        
        q = deque()
        q.append(start)
        prob = [0 for i in range(n)]
        prob[start] = 1
        while q: 
            curr = q.popleft()
            for n in graph[curr]:
                if prob[n[0]]<prob[curr]*n[1]:
                    prob[n[0]] = prob[curr]*n[1]
                    q.append(n[0])
                    
        return prob[end]
                
        
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        
        for i in range(n):
            stones[i] = -stones[i]
        
        heapify(stones)
        
        while stones:
            s1 = -heappop(stones)
            if not stones:
                return s1
            s2 = -heappop(stones)
            if s1>s2:
                heappush(stones,s2-s1)
                
        return 0
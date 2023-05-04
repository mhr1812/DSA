class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r,d,n = deque(),deque(),len(senate)
        
        for i,s in enumerate(senate):
            if s=="R":
                r.append(i)
            else:
                d.append(i)
        
        while r and d:
            r1,d1 = r.popleft(),d.popleft()
            if r1<d1:
                r.append(r1+n)
            else:
                d.append(d1+n)
                
        return "Radiant" if r else "Dire"
            
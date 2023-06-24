class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        sm = sum(rods)
        t = [-1 for i in range(sm+1)]
        t[0] = 0
        
        for e in rods:
            t1 = t[:]
            for i in range(sm-e+1):
                if t1[i]<0:
                    continue
                t[i+e] = max(t[i+e],t1[i])
                t[abs(i-e)] = max(t[abs(i-e)],t1[i]+min(i,e))
        return t[0]
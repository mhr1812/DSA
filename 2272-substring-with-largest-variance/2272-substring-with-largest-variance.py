class Solution:
    def largestVariance(self, s: str) -> int:
        st = set(s)
        pairs = [(e1,e2) for e1 in st for e2 in st if e1!=e2]
        ans=c1=c2= 0
        for _ in range(2):
            for pair in pairs:
                c1=c2=0
                for e in s:
                    if e not in pair:
                        continue
                    if e==pair[0]:
                        c1+=1
                    else:
                        c2+=1
                    if c1<c2:
                        c1=c2=0 
                    elif c1>0 and c2>0:
                        ans = max(ans,c1-c2)
            s = s[::-1]
        return ans
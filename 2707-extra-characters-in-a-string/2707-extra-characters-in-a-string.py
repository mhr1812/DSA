class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        mx = float('inf')
        st = set()
        for e in dictionary:
            st.add(e)
        t = [mx for i in range(n+1)]
        t[0] = 0
        for i in range(1,n+1):
            t[i] = t[i-1]+1
            for j in range(i-1,-1,-1):
                if s[j:i] in st:
                    t[i] = min(t[i],t[j])
        return t[n]
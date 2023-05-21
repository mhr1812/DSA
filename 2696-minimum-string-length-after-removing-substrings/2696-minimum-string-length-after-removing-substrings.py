class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for e in s:
            if e=='B' and st and st[-1]=='A':
                st.pop()
            elif e=='D' and st and st[-1]=='C':
                st.pop()
            else:
                st.append(e)
        return len(st)
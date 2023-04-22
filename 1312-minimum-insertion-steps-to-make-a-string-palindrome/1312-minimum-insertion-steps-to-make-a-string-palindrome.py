class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        t = [0 for i in range(n)]
        for i in range(n-2,-1,-1):
            prev = 0
            for j in range(i+1,n):
                temp = t[j]
                if s[i]==s[j]:
                    t[j] = prev
                else:
                    t[j] = min(t[j],t[j-1])+1
                prev = temp
        return t[n-1]
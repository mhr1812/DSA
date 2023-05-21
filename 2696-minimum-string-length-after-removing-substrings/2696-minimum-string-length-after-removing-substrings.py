class Solution:
    def minLength(self, s: str) -> int:
        ans = len(s)
        while 'AB' in s or 'CD' in s:
            if 'AB' in s:
                s = s.replace('AB','',1)
                ans-=2
            if 'CD' in s:
                s = s.replace('CD','',1)
                ans-=2
        return ans
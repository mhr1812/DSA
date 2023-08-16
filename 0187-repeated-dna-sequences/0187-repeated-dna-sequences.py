class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        mp = {}
        n = len(s)
        for i in range(n-9):
            if s[i:i+10] in mp:
                ans.add(s[i:i+10])
            else:
                mp[s[i:i+10]]=1
        return list(ans)
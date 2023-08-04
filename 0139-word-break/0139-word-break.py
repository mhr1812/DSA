class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        t = [True] + [False]*n
        for i in range(1,n+1):
            for w in wordDict:
                if i-len(w)>=0 and t[i-len(w)] and s[:i].endswith(w):
                    t[i] = True
                    break 
        return t[-1]
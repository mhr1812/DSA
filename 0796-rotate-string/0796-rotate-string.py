class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(0,n):
            if s[i:]+s[:i]==goal:
                return True
        return False
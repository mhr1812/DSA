class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return s in goal+goal and len(s)==len(goal)
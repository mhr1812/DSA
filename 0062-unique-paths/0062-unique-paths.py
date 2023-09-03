class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -=1
        n -=1
        up = 1
        for i in range(m+1, m+n+1):
            up *= i
        down = 1
        for i in range(1, n+1):
            down *= i
        return up//down
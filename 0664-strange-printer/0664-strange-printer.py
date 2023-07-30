class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        t = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            t[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    t[i][j] = t[i][j - 1]
                else:
                    t[i][j] = float('inf')
                    for k in range(i, j):
                        t[i][j] = min(t[i][j], t[i][k] + t[k + 1][j])

        return t[0][n - 1]
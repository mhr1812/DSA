class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        res, c = 0, 1

        def inv(x):
            return pow(x, MOD - 2, MOD)

        for x in range(1, n - k):
            c = (c * -x) % MOD
        c = inv(c)

        for j in range(1, n - k + 1):
            res += pow(j, goal - k - 1, MOD) * c
            c = c * (j - (n - k)) % MOD * inv(j) % MOD

        for j in range(1, n + 1):
            res = res * j % MOD
        return res
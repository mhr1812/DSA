class Solution:
    def distributeCookies(self, cookies, k):
        n = len(cookies)
        v = [0] * k
        res = [float('inf')]
        def dfs(i):
            if i == n:
                m = max(v)
                res[0] = min(res[0], m)
                return 
            for j in range(k):
                v[j] += cookies[i]
                dfs(i + 1)
                v[j] -= cookies[i]
                if v[j] == 0:
                    break
        dfs(0)
        return res[0]
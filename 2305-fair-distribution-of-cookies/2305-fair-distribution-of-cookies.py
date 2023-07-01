class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        arr = [0 for i in range(k)]
        ans = float('inf')
        def dfs(i):
            nonlocal ans
            if i==n:
                ans = min(ans,max(arr))
                return
            for j in range(k):
                arr[j]+=cookies[i]
                dfs(i+1)
                arr[j]-=cookies[i]
                if arr[j]==0:
                    break
        dfs(0)
        return ans
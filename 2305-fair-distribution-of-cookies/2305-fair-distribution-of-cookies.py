class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        arr = [0 for i in range(k)]
        def recur(i):
            nonlocal ans,arr
            if i==len(cookies):
                ans = min(ans,max(arr))
                return 
            if ans<=max(arr):
                return 
            for j in range(k):
                arr[j]+=cookies[i]
                recur(i+1)
                arr[j]-=cookies[i]
            
        recur(0)
        return ans
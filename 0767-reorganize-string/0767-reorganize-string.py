class Solution:
    def reorganizeString(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c]+=1
        arr = [(-v,k) for k,v in d.items()]
        heapq.heapify(arr)
        ans = []
        pf, pc = 0,""
        while arr:
            freq,char = heapq.heappop(arr)
            ans.append(char)
            if pf<0:
                heapq.heappush(arr,(pf,pc))
            freq+=1
            pf,pc = freq,char
        if len(ans)==len(s):
            return "".join(ans)
        return ""
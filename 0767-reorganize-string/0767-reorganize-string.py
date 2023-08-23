class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        pq = [(-count, char) for char, count in collections.Counter(s).items()]
        heapify(pq)

        while pq:
            count, char = heappop(pq)
            if not ans or char != ans[-1]:
                ans.append(char)
                if count + 1 != 0: 
                    heapq.heappush(pq, (count + 1, char))
            else:
                if not pq: return ''
                count_next, char_next = heappop(pq)
                ans.append(char_next)
                if count_next + 1 != 0:
                    heapq.heappush(pq, (count_next + 1, char_next))
                heapq.heappush(pq, (count, char))

        return ''.join(ans)


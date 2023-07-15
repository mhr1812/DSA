class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        events.insert(0, [events[0][0], events[0][1], -sys.maxsize])
        res, sz, end_time = 0, len(events), [0]
        t = [[0 for _ in range(k+1)] for _ in range(sz)]
        for i in range(1, sz):
            idx = bisect_left(end_time, events[i][0])
            for j in range(1, k+1):
                t[i][j] = max(t[i-1][j], t[idx-1][j-1] + events[i][2])
            end_time.append(events[i][1])
        return max(t[sz-1])
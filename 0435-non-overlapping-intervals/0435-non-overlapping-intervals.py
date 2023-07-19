class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[1])
        end = float('-inf')
        cnt = 0
        for interval in intervals:
            s, e = interval
            if s >= end:
                end = e
            else:
                cnt+=1
                
        return cnt
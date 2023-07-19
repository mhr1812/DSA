class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 1:
            return 0
        count = 0
        intervals.sort(key=lambda a:a[0])
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] > intervals[i][0]:
                if intervals[i-1][1] > intervals[i][1]:
                    del intervals[i-1]
                else:
                    del intervals[i]
                count += 1
            else:
                i+=1
        return count
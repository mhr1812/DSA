class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n,prev,c = len(intervals),0,1
        intervals.sort(key = lambda x:x[1])
        for i in range(1,n):
            if intervals[i][0]>=intervals[prev][1]:
                prev = i
                c+=1
        return n-c
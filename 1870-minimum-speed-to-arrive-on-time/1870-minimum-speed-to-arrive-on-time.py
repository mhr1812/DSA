class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        
        if len(dist)-1 >= hour:
            return -1
        
        def helper(speed):
            #print(nan)
            
            total_hour = 0
            for i, d in enumerate(dist):
                if i == len(dist)-1:
                    time_taken = d/speed
                else:
                    time_taken = ceil(d/speed)
                total_hour += time_taken
            #print(speed, total_hour)
            
            return total_hour <= hour
        
        
        l = 1
        #r = max(dist)
        r = 10**9
        
        while l < r:
            m = l + (r-l) // 2
            #print(l,r,m)
            if helper(m):
                r = m
            else:
                l = m + 1
        
        return l
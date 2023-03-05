class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        x = n-1
        time%=2*x
        if time<=x:
            return time+1
        else:
            time%=x
            return n-time
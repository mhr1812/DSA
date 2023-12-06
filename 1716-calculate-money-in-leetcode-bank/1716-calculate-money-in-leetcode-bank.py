class Solution:
    def totalMoney(self, n: int) -> int:
        k = n//7
        m = n%7
        sm = 0
        for i in range(k+1,k+m+1):
            sm+=i
        st = 1
        end = 7
        while st<=k:
            for i in range(st,end+1):
                sm+=i
            st+=1
            end+=1
        return sm
        
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        t = {}
        def recur(i,k):
            #memoization
            if (i,k) in t:
                return t[(i,k)]
            #base case
            if k==0 or i==len(piles):
                return 0
            recur(i+1,k)
            #not selecting from current pile
            ans,cur = recur(i+1,k),0
            #selecting from current pile
            for j in range(min(k,len(piles[i]))):
                cur+=piles[i][j]
                ans = max(ans,cur+recur(i+1,k-j-1))
            t[(i,k)] = ans
            return t[(i,k)]
        return recur(0,k)
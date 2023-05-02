class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        A = [0] + cuts + [n]
        
        def dfs(i, j, A, dp):
            if i > j:
                return 0
			# check the memoization cache
            if dp[i][j] != -1:
                return dp[i][j]
            
            mini = float("inf")
            for k in range(i, j+1):
                cost = A[j+1]-A[i-1] + dfs(i, k-1, A, dp) + dfs(k+1, j, A, dp)
                mini = min(cost, mini)
            
			# set the computed value so we don't have to recompute
            dp[i][j] = mini
            return mini
                
		# build our len(cuts)*len(cuts) 2D array cache
        dp = [[-1 for j in range(len(cuts)+1)] for i in range(len(cuts)+1)]
        
        res = dfs(1, len(cuts), A, dp)
        return res
        
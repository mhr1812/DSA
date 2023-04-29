class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sm = sum(nums)
        if sm<abs(target) or (sm+target)%2!=0: return 0
        s1 = (sm+target)//2
        
        def perfectSum(arr,sm):
            n = len(arr)
            t = [[0 for j in range(sm+1)]for i in range(n+1)]
            
            for j in range(sm+1):
                t[0][j] = 0
            t[0][0] = 1
            
            for i in range(1,n+1):
                for j in range(sm+1):
                    if arr[i-1]<=j:
                        t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]
                    else:
                        t[i][j] = t[i-1][j]
            return t[n][sm]
        
        return perfectSum(nums,s1)
        
        
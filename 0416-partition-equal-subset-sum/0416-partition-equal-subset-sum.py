class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subsetSum(arr,sum):
            n = len(arr)
            t = [[-1 for j in range(sum+1)]for i in range(n+1)]    
            for j in range(sum+1):
                t[0][j] = False
            for i in range(n+1):
                t[i][0] = True
            for i in range(1,n+1):
                for j in range(1,sum+1):
                    if arr[i-1]<=j:
                        t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
                    else:
                        t[i][j] = t[i-1][j]
            return t[n][sum]
        
        sm = sum(nums)
        if sm%2==1:
            return False
        else:
            return subsetSum(nums,sm//2)
        
        
            
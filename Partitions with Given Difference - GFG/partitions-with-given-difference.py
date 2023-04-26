#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
mod = pow(10,9)+7
class Solution:
    def countPartitions(self, n, d, arr):
        # Code here
        sm = sum(arr)
        if (d+sm)%2!=0: return 0
        s1 = (d+sm)//2
        def perfectSum(arr,sm):
            n = len(arr)
            t = [[0 for j in range(sm+1)]for i in range(n+1)]
            for j in range(sm+1):
                t[0][j] = 0
            t[0][0] = 1
            for i in range(1,n+1):
                for j in range(sm+1):
                    if arr[i-1]<=j:
                        t[i][j] = (t[i-1][j-arr[i-1]] + t[i-1][j])%mod
                    else:
                        t[i][j] = t[i-1][j]
                    
            return t[n][sm]%mod
        return perfectSum(arr,s1)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, d = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countPartitions(n, d, arr)
        print(res)
# } Driver Code Ends
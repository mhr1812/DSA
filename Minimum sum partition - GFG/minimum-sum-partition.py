#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		# code here
        def subset(arr,sm):
            n = len(arr)
            t = [[-1 for j in range(sm+1)]for i in range(n+1)]
            for j in range(sm+1):
                t[0][j] = False
            for i in range(n+1):
                t[i][0] = True
            for i in range(1,n+1):
                for j in range(1,sm+1):
                    if arr[i-1]<=j:
                        t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
                    else:
                        t[i][j] = t[i-1][j]
            v = []
            for j in range(sm//2+1):
                if t[n][j]: v.append(j)
            return v 
        nums = subset(arr,sum(arr))
        mn = 1e18
        for i in range(len(nums)-1,-1,-1):
            mn = min(mn,sum(arr)-2*nums[i])
        return mn

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends
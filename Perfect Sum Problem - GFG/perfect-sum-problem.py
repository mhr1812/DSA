#User function Template for python3
m = int(1e9+7)
class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		t = [[0 for j in range(sum+1)]for i in range(n+1)]
		for j in range(sum+1):
		    t[0][j] = 0
		t[0][0] = 1
		for i in range(1,n+1):
		    for j in range(0,sum+1):
		        if arr[i-1]<=j:
		            t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
		        else:
		            t[i][j] = t[i-1][j]
		        t[i][j]%=m
		return t[n][sum]%m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends
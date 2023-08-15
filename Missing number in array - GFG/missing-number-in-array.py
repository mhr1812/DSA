#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        # code here
        sm = n*(n+1)//2
        sm1 = sum(array)
        return sm-sm1


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends
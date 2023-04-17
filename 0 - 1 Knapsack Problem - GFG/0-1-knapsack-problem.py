#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        t = [[-1 for j in range(W+1)]for i in range(n+1)]
       
        # # code here
        # def recur(W,wt,val,n):
        #     if n==0 or W==0:
        #         return 0
        #     if t[n][W]!=-1:
        #         return t[n][W]
        #     if wt[n-1]<=W:
        #         return max(val[n-1]+recur(W-wt[n-1],wt,val,n-1), recur(W,wt,val,n-1))
        #     else:
        #         return recur(W,wt,val,n-1)
        # return recur(W,wt,val,n)
        for i in range(n+1):
            t[i][0] = 0
        for j in range(W+1):
            t[0][j] = 0
        for i in range(1,n+1):
            for j in range(1,W+1):
                if wt[i-1]<=j:
                    t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        return t[n][W]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends
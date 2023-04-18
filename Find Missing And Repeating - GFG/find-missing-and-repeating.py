#User function Template for python3
from collections import Counter
class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        c = Counter(arr)
        x,y = -1,-1
        for i in range(n):
            if c[i+1]==0:
                x = i+1
            elif c[i+1]==2:
                y = i+1
            if x>0 and y>0:
                return (y,x)
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends
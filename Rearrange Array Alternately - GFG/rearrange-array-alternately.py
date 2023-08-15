#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        l,r = 0,n-1
        mx = arr[n-1]+1
        for i in range(n):
            if i%2==0:
                arr[i] += (arr[r]%mx)*mx
                r-=1
            else:
                arr[i]+=(arr[l]%mx)*mx
                l+=1
        for i in range(n):
            arr[i]//=mx
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
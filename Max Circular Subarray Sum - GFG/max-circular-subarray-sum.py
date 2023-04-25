#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr,n):
    ##Your code here
    if (n == 1):
        return arr[0]
        
    mini,maxi,curr_min,curr_max = arr[0],arr[0],arr[0],arr[0]
    sm = sum(arr)
    
    for i in range(1,n):
        curr_max = max(curr_max+arr[i],arr[i])
        maxi = max(maxi,curr_max)
        
        curr_min = min(curr_min+arr[i],arr[i])
        mini = min(mini,curr_min)
    if mini==sm:
        return maxi
        
    return max(maxi,sm-mini)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math
import sys

    
    

if __name__ == "__main__":
    T=int(input())
    while(T>0):
            
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
            
        print(circularSubarraySum(arr,n))
        
        T-=1
    
# } Driver Code Ends
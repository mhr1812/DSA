#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        L,R = [],[]
        for i in range(m-l+1):
            L.append(arr[l+i])
        for i in range(r-m):
            R.append(arr[m+1+i])
        i,j,k = 0,0,l
        while i<m-l+1 and j<r-m:
            if L[i]<=R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i<m-l+1:
            arr[k] = L[i]
            i+=1
            k+=1
        while j<r-m:
            arr[k] = R[j]
            j+=1
            k+=1
        
    def mergeSort(self,arr, l, r):
        #code here
        if l<r:
            mid = l+(r-l)//2
            self.mergeSort(arr,l,mid)
            self.mergeSort(arr,mid+1,r)
            self.merge(arr,l,mid,r)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        pivot = 1
        i,start,end = 0,0,n-1
        while i<=end:
            if arr[i]<pivot:
                arr[i],arr[start] = arr[start],arr[i]
                start+=1
                i+=1
            elif arr[i]>pivot:
                arr[i],arr[end] = arr[end],arr[i]
                end-=1
            else:
                i+=1
        return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
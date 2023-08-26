
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        l = [0]*n
        r = [0]*n
        l[0] = arr[0]
        for i in range(1,n):
            l[i] = max(l[i-1],arr[i])
        r[-1] = arr[-1]
        for i in range(n-2,-1,-1):
            r[i] = max(r[i+1],arr[i])
        ans = 0
        for i in range(n):
            ans+=min(l[i],r[i])-arr[i]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends
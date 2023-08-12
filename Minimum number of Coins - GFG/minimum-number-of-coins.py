#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        coins = [1,2,5,10,20,50,100,200,500,2000]
        i = len(coins)-1
        ans = []
        while i>=0:
            if coins[i]<=N:
                ans.append(coins[i])
                N-=coins[i]
            else:
                i-=1
            if N==0:
                break
                        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
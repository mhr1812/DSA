#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        #code here
        length = []
        for i in range(n):
            length.append(i+1)
        
        t = [[0 for j in range(n+1)]for i in range(n+1)]
        
        for i in range(n+1):
            t[i][0] = 0
        
        for j in range(n+1):
            t[0][j] = 0
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                if length[i-1]<=j:
                    t[i][j] = max(t[i-1][j], price[i-1]+ t[i][j-length[i-1]])
                else:
                    t[i][j] = t[i-1][j]
        return t[n][n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
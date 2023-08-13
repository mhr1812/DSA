#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, S):
        # code here
        d = {}
        ans,n,start = 0,len(S),0
        for i in range(n):
            if S[i] in d:
                start = max(start, d[S[i]]+1)
            ans = max(ans,i-start+1)
            d[S[i]] = i
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends
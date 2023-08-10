#User function Template for python3
from collections import defaultdict
class Solution:

    def firstRepChar(self, s):
        # code here
        n = len(s)
        d = defaultdict(int)
        for i in range(n):
            d[s[i]]+=1
            if d[s[i]]>1:
                return s[i]
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.firstRepChar(s))
# } Driver Code Ends
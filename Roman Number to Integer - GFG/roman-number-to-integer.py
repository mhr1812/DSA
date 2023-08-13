#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        # code here
        d = {'I':1,
            'V' :5,
            'X': 10,
            'L': 50,
            'C' :100,
            'D' :500,
            'M' :1000}
        ans,n,i = 0,len(S),0
        while i<n:
            if i<n-1 and d[S[i]]<d[S[i+1]] :
                ans+=d[S[i+1]]-d[S[i]]
                i+=1
            else:
                ans+=d[S[i]]
            i+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends
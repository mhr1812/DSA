#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        ans = arr[0]
        def common(s1,s2):
            n,m = len(s1),len(s2)
            res = ""
            for i in range(min(n,m)):
                if s1[i]!=s2[i]:
                    break
                res+=s1[i]
            return res
        for i in range(1,len(arr)):
            ans = common(ans,arr[i])
        if ans=="":
            return -1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends
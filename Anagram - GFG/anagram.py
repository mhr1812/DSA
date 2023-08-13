#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        d = {}
        if len(a)!=len(b):
            return False
        n = len(a)
        for i in range(n):
            if a[i] in d:
                d[a[i]]+=1
            else:
                d[a[i]] = 1
        for i in range(n):
            if b[i] in d and d[b[i]]>0:
                d[b[i]]-=1
            else:
                return False
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends
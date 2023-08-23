#User function Template for python3
from collections import defaultdict
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        d = defaultdict(int)
        for a in A:
            d[a]+=1
        for b in B:
            if d[b]<1:
                return False
            d[b]-=1
        return True
            
        
        #return: True or False
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends
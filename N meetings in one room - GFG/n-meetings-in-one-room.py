#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        p = []
        for i in range(n):
            p.append([start[i],end[i]])
        
        p.sort(key=lambda x:x[1])
        ans = 1
        time_limit = p[0][1]
        for i in range(1,n):
            if p[i][0]>time_limit:
                time_limit = p[i][1]
                ans+=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends
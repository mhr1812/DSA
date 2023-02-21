#User function Template for python3

class Solution:
    def absDifOne(self, N):
        # code here
        ans = []
        for num in range(1,10):
            queue = []
            queue.append(num)
            
            while queue:
                curr = queue[0]
                queue.pop(0)
                if curr>9 and curr<=N:
                    ans.append(curr)
                if curr>N:
                    continue
                
                last = curr%10
                num1 = curr*10+last-1
                num2 = curr*10+last+1
                
                if last==0:
                    queue.append(num2)
                elif last==9:
                    queue.append(num1)
                else:
                    queue.append(num1)
                    queue.append(num2)
        if not ans:
            return [-1]
        else:
            return sorted(ans)
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        
        ob=Solution()
        answer = ob.absDifOne(n)
        for value in answer:
            print(value, end = ' ')
        
        if len(answer) == 0:
            print(-1)
        else:
            print()
# } Driver Code Ends
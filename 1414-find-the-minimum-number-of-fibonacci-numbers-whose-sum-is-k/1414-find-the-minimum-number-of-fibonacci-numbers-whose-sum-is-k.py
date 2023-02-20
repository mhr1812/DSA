class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1,1]
        
        while fib[-1]<=k:
            fib.append(fib[-1]+fib[-2])
        
        ans,l = 0,len(fib)-1
        
        while k>0:
            if fib[l]<=k:
                k-=fib[l]
                ans+=1
            l-=1
        
        return ans
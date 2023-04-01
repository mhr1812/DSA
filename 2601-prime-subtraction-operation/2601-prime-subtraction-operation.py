class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def sieve(num):
            prime = [True for i in range(num+1)]
            prime[0] = prime[1] = False
            
            for i in range(2,int(sqrt(num)+1)):
                if prime[i]:
                    for j in range(i*i,num+1,i):
                        prime[j] = False
            return [i for i in range(1,num+1) if prime[i]]
        primes = sieve(1000)
        
        n = len(nums)
        prev = 0
        for i in range(n):
            x = nums[i] - prev - 1
            idx = bisect_left(primes,x)
            takeCurr = False
            if idx>=len(primes) or primes[idx]>x:
                if idx>0 and primes[idx-1]<=x:
                    idx -=1
                else:
                    takeCurr = True
            curr = nums[i]
            if not takeCurr:  
                curr = nums[i]-primes[idx]
            if curr <= prev:  
                return False
            prev = curr
        return True

        
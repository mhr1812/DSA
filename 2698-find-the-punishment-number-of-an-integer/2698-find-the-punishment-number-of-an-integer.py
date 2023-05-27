class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check(s1,s2,n,target):
            if not n:
                return target==s1+s2 
            num = int(n[0])
            return check(s1,10*s2+num,n[1:],target) or check(s1+s2,num,n[1:],target)
        ans = 0
        for i in range(1,n+1):
            if check(0,0,str(i*i),i):
                ans+=i*i 
        return ans
    
        
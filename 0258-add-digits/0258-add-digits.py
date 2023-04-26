class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        ans = 0
        if len(num)==1:
            return int(num)
        while len(num)>1:
            x = 0
            for e in num:
                x+=int(e)
            ans = x
            num = str(x)
        return ans
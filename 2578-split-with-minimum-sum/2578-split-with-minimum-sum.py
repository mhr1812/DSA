class Solution:
    def splitNum(self, num: int) -> int:
        y = str(num)
        n = ''.join(sorted(y))
        x = len(n)
        n1,n2 = "",""
        for i in range(x):
            if i%2==0:
                n1 += n[i]
            else:
                n2 += n[i]
        ans = int(n1) + int(n2)
        return ans
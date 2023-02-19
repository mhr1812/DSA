class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        l = len(s)
        for i in range(l):
            if s[i]!='9':
                break
        if i!=l:
            maxi = int(s.replace(s[i],'9'))
        else:
            maxi = num
        mini = int(s.replace(s[0],'0'))
        return maxi-mini
        
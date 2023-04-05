class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        d = sorted(c.items(),key= lambda x:x[1],reverse=True)
        l = []
        for i in range(len(d)):
            l.append([d[i][0],d[i][1]])
        a = []
        n = l[0][1]
        for i in range(n):
            b = []
            for j in range(len(c)):
                if l[j][1]>0:
                    b.append(l[j][0])
                    l[j][1]-=1
            a.append(b)
        return a
            
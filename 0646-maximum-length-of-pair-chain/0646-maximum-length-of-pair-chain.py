class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        c = 1
        pairs.sort(key = lambda x:x[1])
        prev = pairs[0][1]
        for i in range(len(pairs)):
            if pairs[i][0]>prev:
                c+=1
                prev = pairs[i][1]
        return c
            
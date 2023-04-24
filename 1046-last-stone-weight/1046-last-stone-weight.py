class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        n = len(stones)
        while 1:
            if len(stones)<=1:
                break
            if stones[-1]==stones[-2]:
                stones.pop()
                stones.pop()
            else:
                if stones[-1]<stones[-2]:
                    stones[-2]-=stones[-1]
                    stones.pop()
                else:
                    stones[-1]-=stones[-2]
                    stones.pop(len(stones)-2)
            stones.sort()
        if len(stones)==1:
            return stones[0]
        return 0
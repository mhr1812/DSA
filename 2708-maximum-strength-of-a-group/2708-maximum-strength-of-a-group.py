class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        f = 0
        pos,neg = [],[]
        
        for e in nums:
            if e>0:
                pos.append(e)
            elif e<0:
                neg.append(e)
            else:
                f = 1 
        if len(neg)%2==1:
            if len(neg)>1:
                neg.remove(max(neg))
            elif pos:
                return math.prod(pos)
            elif f:
                return 0
            else:
                return max(neg)
            
        if not pos and not neg:
            return 0 
        return math.prod(pos)*math.prod(neg)
        
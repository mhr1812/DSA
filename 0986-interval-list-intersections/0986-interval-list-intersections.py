class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        n,m = len(firstList), len(secondList)
        i,j = 0,0
        
        while i<n and j<m:
            a1,a2 = firstList[i]
            b1,b2 = secondList[j]
            
            if a1<=b2 and b1<=a2:
                ans.append([max(a1,b1),min(a2,b2)])
            
            if a2<b2:
                i+=1
            else:
                j+=1
        return ans
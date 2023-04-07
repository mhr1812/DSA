class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        ans = []
        for i in range(len(heights)):
            d[heights[i]] = names[i]
        heights.sort(reverse=True)
        for h in heights:
            ans.append(d[h])
        return ans
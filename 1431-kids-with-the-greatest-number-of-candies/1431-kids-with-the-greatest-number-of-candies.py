class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        result = [False for i in range(len(candies))]
        for i in range(len(candies)):
            if candies[i]+extraCandies >= mx:
                result[i]= True
        return result
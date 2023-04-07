class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        _,names = zip(*sorted(zip(heights,names), reverse = True)) 
        return  list(names)
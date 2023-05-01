class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        mn,mx = min(salary),max(salary)
        sm = sum(salary)
        return (sm-mn-mx)/(n-2)
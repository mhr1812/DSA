class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        salary.sort()
        sm = sum(salary[1:n-1])
        return sm/(n-2)
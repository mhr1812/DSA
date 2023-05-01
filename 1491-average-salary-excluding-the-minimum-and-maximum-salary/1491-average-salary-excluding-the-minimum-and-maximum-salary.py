class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)-2
        return (sum(salary)-min(salary)-max(salary))/(n)
from numpy import array, ceil, sum

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def check(speed: float) -> bool:
            time = array(dist) / speed
            time = ceil(time)
            time[-1] = dist[-1] / speed
            return sum(time) <= hour

        # Check that the solution exists
        if len(dist) > ceil(hour):
            return -1

        # Binary search
        unfeasible, solution = 0, 10**7
        while solution - unfeasible > 1:
            mid = (unfeasible + solution) // 2
            if check(mid):
                solution = mid
            else:
                unfeasible = mid

        return solution
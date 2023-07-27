class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batlen = len(batteries)
        batteries.sort(reverse=True)
        m, M = 0, sum(batteries) // n
        while m < M:
            mm = (m + M + 1) // 2
            j = 0
            curr = 0
            prev = 0
            leftOver = 0
            success = True
            for i in range(n):
                while curr < mm and j < batlen:
                    add = min(batteries[j], mm - curr)
                    prev = curr
                    curr += add
                    leftOver = batteries[j] - add
                    j += 1
                if curr < mm:
                    success = False
                    break

                if leftOver <= prev:
                    curr = leftOver
                else:
                    curr = 0
            if success:
                m = mm
            else:
                M = mm-1
        return m
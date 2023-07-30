class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        @cache
        def func(left, right): 
            if left >= right: 
                return 0
            best = func(left + 1, right) + 1
            for i in range(left + 1, right + 1): 
                if s[left] == s[i]: 
                    best = min(best, func(left, i - 1) + func(i, right))
            return best
        return func(0, n - 1) + 1
        
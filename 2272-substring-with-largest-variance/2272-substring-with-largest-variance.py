class Solution:
    def largestVariance(self, s: str) -> int:
        counter = collections.Counter(s)
        res = 0
        for a, b in itertools.permutations(counter, 2):
            has_a, has_b = False, False
            a_left, b_left = counter[a], counter[b]
            total = 0
            for ch in s:
                if ch != a and ch != b:
                    continue
                if total < 0 and a_left and b_left:
                    total = 0
                    has_a, has_b = False, False
                if ch == a:
                    has_a = True
                    a_left -= 1
                    total += 1
                if ch == b:
                    has_b = True
                    b_left -= 1
                    total -= 1
                if has_a and has_b:
                    res = max(res, total)

        return res
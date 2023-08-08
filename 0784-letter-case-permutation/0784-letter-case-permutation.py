class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def backtrack(s):
            if not s:
                return ['']
            perm = backtrack(s[1:])
            if s[0].isdigit():
                return map(lambda x: s[0] + x, perm)
            else:
                res = []
                for word in perm:
                    res.append(s[0].lower() + word)
                    res.append(s[0].upper() + word)
                return res

        return backtrack(s)
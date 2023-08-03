class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        ans = []
        def recur(idx, comb):
            if idx == len(digits):
                ans.append(comb)
                return
            
            for letter in d[digits[idx]]:
                recur(idx + 1, comb + letter)
        
        recur(0, "")

        return ans
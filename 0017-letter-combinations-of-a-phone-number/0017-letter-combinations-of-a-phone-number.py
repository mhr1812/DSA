class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # base case: no digits
        if not digits:
            return []

        # create hashmap (dict) to store phone digit (key) and corresponding letters (value)
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        # helper function backtrack to do backtracking
        def backtrack(combination, next_digits):
            # if no more digits to process, append current combination to res list and return
            if not next_digits:
                res.append(combination)
                return

            # otherwise iterate through each letter that the first remaining digit maps to
            # recursively call backtrack with new combination & remaining digits
            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

        backtrack("", digits)
        return res
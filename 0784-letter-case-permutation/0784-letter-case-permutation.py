class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans,n = [],len(s)
        def recur(sub="",i=0):
            if len(sub)==n:
                ans.append(sub)
            else:
                if s[i].isalpha():
                    recur(sub+s[i].swapcase(),i+1)
                recur(sub+s[i],i+1)
        recur()
        return ans
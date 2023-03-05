class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n,x = len(word),0
        ans = [0 for i in range(n)]
        for i in range(n):
            x =(10*x+int(word[i]))%m 
            if x%m==0:
                ans[i] = 1
            else:
                ans[i] = 0
        return ans
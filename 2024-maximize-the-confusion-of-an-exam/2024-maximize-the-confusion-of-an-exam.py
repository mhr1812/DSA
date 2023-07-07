class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        prev = ans = 0
        n = len(answerKey)
        d = defaultdict(int)
        for i in range(n):
            d[answerKey[i]]+=1
            ans = max(ans,d[answerKey[i]])
            if i-prev+1>ans+k:
                d[answerKey[prev]]-=1
                prev+=1
        return n-prev
                
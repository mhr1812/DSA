class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, target: int) -> int:
        mx=0
        for ch in "TF":
            j=0
            k=target
            for i in answerKey:
                if i==ch:k-=1
                if k<0:
                    if answerKey[j]==ch:k+=1
                    j+=1
            mx=max(mx,len(answerKey)-j)
        return mx
                
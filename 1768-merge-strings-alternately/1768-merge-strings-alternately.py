class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m = len(word1),len(word2)
        if m<=n:
            x = 1
            for i in range(m):
                word1 = word1[:x]+word2[i]+word1[x:]
                x+=2
        else:
            x = 1
            for i in range(n):
                word1 = word1[:x]+word2[i]+word1[x:]
                x+=2
            word1 = word1+word2[n:]
        return word1
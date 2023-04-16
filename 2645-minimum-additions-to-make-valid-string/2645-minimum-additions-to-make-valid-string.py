class Solution:
    def addMinimum(self, word: str) -> int:
        i,ans = 0,0
        while i<len(word):
            if word[i:i+3]=="abc":
                i+=3
            elif word[i:i+2] in ['ab','bc','ac']:
                ans+=1
                i+=2
            else:
                ans+=2
                i+=1
                
        return ans
        
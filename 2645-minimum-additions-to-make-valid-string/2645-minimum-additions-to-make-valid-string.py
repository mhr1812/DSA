class Solution:
    def addMinimum(self, word: str) -> int:
        word = word.replace("abc"," ")
        x = word.count("ab")+ word.count("bc")+word.count("ac")
        y = word.count("c") + word.count("a") + word.count("b")
                
        return 2*y-3*x
        
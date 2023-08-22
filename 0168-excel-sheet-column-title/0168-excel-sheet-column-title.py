class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber<27:
            return chr(64+columnNumber)
        ans = ""
        while columnNumber>0:
            if columnNumber%26==0:
                ans+='Z'
                columnNumber-=1
            else:
                ans+=chr(64+columnNumber%26)
            columnNumber//=26
        return ans[::-1]
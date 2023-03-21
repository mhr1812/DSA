class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money<children:
            return -1
        x = 8*children - money
        if x<=0:
            return children - (x<0)
        
        ans, rem = divmod(money-children,7)     #   <-- Every child gets a dollar, then ans
                                                #       children get an additional 7 dollars 

        return ans - ((ans, rem) == (children - 1, 3))
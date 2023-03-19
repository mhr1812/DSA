class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        x = bin(n)[2:]
        x = str(x)
        x = x[::-1]
        even,odd = 0,0
        for i in range(len(x)):
            if x[i]=='1':
                if i%2==0:
                    even+=1
                else:
                    odd+=1
        return (even,odd)
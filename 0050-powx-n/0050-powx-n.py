class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1/self.myPow(x, -n)

        if n % 2 == 1:
            # odd
            return x * self.myPow(x*x, n//2)
        else:
            # even
            return self.myPow(x*x, n//2)
            
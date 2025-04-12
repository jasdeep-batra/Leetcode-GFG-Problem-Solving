class Solution:
    def myPow(self, x: float, n: int) -> float:
        #final answer will not gonna be more than 10000
        if n ==0:
            return 1
        
        if n < 0:
            x = 1/x
            n = abs(n)
        
        if n%2==0:
            n//=2
            x*=x
            return self.myPow(x,n)
        
        return x*self.myPow(x,n-1)




        
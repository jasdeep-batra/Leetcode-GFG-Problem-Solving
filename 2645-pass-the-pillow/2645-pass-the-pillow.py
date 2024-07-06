class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        dirr = time//(n-1)
        if dirr%2==0:
            return time%(n-1)+1
            
        else:
            return n-time%(n-1)

        
        
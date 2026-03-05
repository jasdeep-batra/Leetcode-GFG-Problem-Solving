class Solution:
    def mySqrt(self, x: int) -> int:
        i,j = 0,x
        while j>=i:
            mid = (j+i)//2
            if mid*mid <= x:
                i = mid+1
            else:
                j = mid-1
        return j




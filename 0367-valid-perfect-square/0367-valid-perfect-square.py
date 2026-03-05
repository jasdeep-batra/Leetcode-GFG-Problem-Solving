class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i,j = 0,num
        while j>=i:
            mid= (j+i)//2
            if mid*mid == num:
                return True
            if mid*mid <= num:
                i = mid+1
            else:
                j = mid-1

        return False
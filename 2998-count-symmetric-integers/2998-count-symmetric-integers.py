class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            num = str(i)
            if len(num)%2==0:
                if sum(map(int,num[:len(num)//2]))==sum(map(int,num[len(num)//2:])):
                    count+=1
        return count

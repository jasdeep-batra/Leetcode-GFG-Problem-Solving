class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        ind = 0
        while(len(arr)!=1):
            i = (ind+ k-1)%len(arr);
            arr.pop(i)
            ind=i

        return arr[0]


        
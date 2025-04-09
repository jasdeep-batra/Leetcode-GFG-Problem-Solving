class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arr = [0]*101
        for index in nums:
            arr[index]=1

        st = k+1
        if k not in nums:
            st = k
        
        cnt = 0
        summ = sum(arr) - (1 if k in nums else 0)
        for i in range(st,len(arr)):
            if arr[i]>0:
                cnt+=1
        return -1 if cnt < summ else cnt

        
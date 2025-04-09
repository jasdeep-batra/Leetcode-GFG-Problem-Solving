class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        #if any num smaller then k then return -1
        # if k in nums then ans-1
        # if not then ans
        dictt = [0]*101
        for index in nums:
            dictt[index] = 1
        cnt = 0
        flag = False
        for i in range(101):
            if dictt[i]==1 and (i < k):
                return -1
            if dictt[i]==1 and i>=k:
                if i==k:
                    flag = True
                cnt+=1

        if flag:
            return cnt-1
        return cnt
                

        
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        #if any num smaller then k then return -1
        # if k in nums then ans-1
        # if not then ans
        dictt = Counter(nums)
        cnt = 0
        flag = False
        for i,v in dictt.items():
            if i < k:
                return -1
            if i>=k:
                if i==k:
                    flag = True
                cnt+=1

        if flag:
            return cnt-1
        return cnt
                

        
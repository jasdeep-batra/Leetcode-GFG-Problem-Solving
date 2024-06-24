class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        dq = deque()
        for i in range(len(nums)):
            while dq and i > dq[0]+k-1:
                dq.popleft()
            if (nums[i]+len(dq))%2==0:
                if i+k > len(nums):
                    return -1
                dq.append(i)
                res+=1
        return res



        
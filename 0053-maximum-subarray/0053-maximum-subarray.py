class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxsum = 0
        res = -10000
        for i in range(len(nums)):
            summ+=nums[i]
            maxsum = max(summ,0)
            res = max(res,maxsum)
            summ = max(summ,maxsum)  #reset
        return res if res>0 else max(nums)


        
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        summ = nums[0] 
        max_summ = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                summ+=nums[i]
                max_summ = max(summ,max_summ)
            else:
                max_summ = max(summ,max_summ)
                summ = nums[i]


        return max_summ
        
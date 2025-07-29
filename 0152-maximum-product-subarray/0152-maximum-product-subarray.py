class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = nums[0]
        minprod = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            temp = maxprod
            maxprod  = max(temp*nums[i],minprod*nums[i],nums[i])
            minprod = min(temp*nums[i],nums[i],minprod*nums[i])
            res = max(maxprod,res)
        return res

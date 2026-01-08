class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_arr = [1]*len(nums)
        prod = nums[0]
        for i in range(1,len(nums)):
            prod_arr[i] = prod
            prod = prod*nums[i]

        prod = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            prod_arr[i]*=prod
            prod*=nums[i]

        return prod_arr
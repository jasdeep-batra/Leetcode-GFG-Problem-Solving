class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
        # z = -1

        z = nums.count(0)

        return [item for item in nums if item!=0]+[0]*z


        
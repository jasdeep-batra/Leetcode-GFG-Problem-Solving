class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        max_num = max(nums)
        diff = 0
        ops = 0
        print(nums)
        # if len(nums)==1:
        #     return 1
        for i in range(len(nums)):
            if nums[i]==0 or (i>0 and nums[i]==nums[i-1]):
                continue
            diff=(nums[i]-nums[i-1])
            ops+=1
            if diff >= max_num:
                return ops
        return ops
            
            
